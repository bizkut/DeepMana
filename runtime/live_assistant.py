"""
Live Assistant - Real-time Hearthstone AI Coach.
Watches game logs, analyzes state with AlphaZero, and displays suggestions via overlay.
"""

import sys
import time
import threading
from typing import Optional

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QThread, pyqtSignal

from overlay.overlay_window import OverlayWindow
from overlay.geometry import HearthstoneGeometry, Point
from runtime.log_watcher import LogWatcher
from runtime.parser import LogParser
from ai.game_state import GameState
from simulator.game import Game
from simulator.player import Player

class AssistantWorker(QThread):
    """Background worker that watches logs and updates the AI state."""
    
    # Signals to update GUI safely
    status_signal = pyqtSignal(str)
    info_signal = pyqtSignal(str)
    winrate_signal = pyqtSignal(float)
    mana_signal = pyqtSignal(int, int)  # current, max
    arrow_signal = pyqtSignal(object, object)
    highlight_signal = pyqtSignal(object)
    
    def __init__(self, use_model: bool = True):
        super().__init__()
        self.running = True
        self.game = Game()
        self.geometry = HearthstoneGeometry()
        
        # Initialize players
        p1 = Player("Player 1")
        p2 = Player("Opponent")
        self.game.players = [p1, p2]
        self.game.current_player_idx = 0
        
        # Parser with state change callback
        self.parser = LogParser(self.game, on_state_change=self._on_game_state_changed)
        self.watcher = LogWatcher(self.handle_log_line)
        
        # AI Brain
        self.use_model = use_model
        self.brain = None
        if use_model:
            try:
                from ai.brain import AIBrain
                self.brain = AIBrain()
                if self.brain.load_latest_model():
                    print("[Assistant] AlphaZero model loaded!")
                else:
                    print("[Assistant] No trained model found. Using simple heuristics.")
                    self.brain = None
            except Exception as e:
                print(f"[Assistant] Failed to load AI Brain: {e}")
                self.brain = None
        
        # Throttle analysis to avoid spam
        self.last_analysis_time = 0
        self.analysis_cooldown = 0.5  # seconds
        
    def run(self):
        """Main loop in thread."""
        self.status_signal.emit("SEARCHING...")
        self.info_signal.emit("Looking for Hearthstone logs...")
        
        # Run watcher in separate thread (it's blocking)
        self.watcher_thread = threading.Thread(target=self.watcher.start, daemon=True)
        self.watcher_thread.start()
        
        # Main loop - periodic refresh
        while self.running:
            time.sleep(0.5)
            
            # Check if we have a game running
            if self.parser.in_game:
                # Throttled analysis
                if time.time() - self.last_analysis_time > self.analysis_cooldown:
                    if self.parser.is_local_player_turn():
                        self.think_and_suggest()
                    else:
                        self.status_signal.emit("OPPONENT'S TURN")
                        self.info_signal.emit("Waiting for opponent...")
                        self.arrow_signal.emit(None, None)
                        self._update_mana()

    def stop(self):
        """Stop the assistant."""
        self.running = False
        self.watcher.stop()
    
    def _on_game_state_changed(self):
        """Called by parser when game state changes."""
        self.last_analysis_time = 0  # Force immediate re-analysis
        
    def _update_mana(self):
        """Update mana display."""
        local_player = self.parser.get_local_player()
        if local_player:
            self.mana_signal.emit(local_player.mana, local_player.max_mana)
    
    def handle_log_line(self, line: str):
        """Called for every new log line."""
        self.parser.parse_line(line)

    def think_and_suggest(self):
        """AI Logic - Uses AlphaZero model if available."""
        self.last_analysis_time = time.time()
        
        if not self.parser.in_game:
            self.status_signal.emit("STANDBY")
            self.info_signal.emit("Waiting for game to start...")
            return

        local_player = self.parser.get_local_player()
        if not local_player:
            self.status_signal.emit("ANALYZING...")
            self.info_signal.emit("Detecting players...")
            return
            
        # Update mana display
        self._update_mana()
        
        # Get perspective (1 = local player is P1, 2 = local player is P2)
        perspective = 1 if self.parser.local_player_id in [None, 1] else 2
        state = GameState.from_simulator_game(self.game, perspective=perspective)
        
        # === USE ALPHAZERO MODEL ===
        if self.brain is not None:
            self._suggest_with_brain(state, local_player)
            return

        # === FALLBACK HEURISTIC AI ===
        self._suggest_heuristic(local_player)

    def _suggest_with_brain(self, state: GameState, local_player):
        """Use trained AlphaZero model for suggestions."""
        from ai.actions import ActionType
        
        action, confidence, description = self.brain.suggest_action(state)
        
        if action is None:
            self.status_signal.emit("WAITING...")
            self.info_signal.emit(description)
            return
        
        conf_pct = int(confidence * 100)
        self.status_signal.emit(description.upper())
        self.info_signal.emit(f"Confidence: {conf_pct}%")
        
        # Get value estimate
        value = self.brain.get_value_estimate(state)
        self.winrate_signal.emit(value)
        
        # Visualize the action
        if action.action_type == ActionType.END_TURN:
            self.arrow_signal.emit(None, None)
            self.highlight_signal.emit(None)
            
        elif action.action_type == ActionType.PLAY_CARD:
            if action.card_index is not None and action.card_index < len(local_player.hand):
                hand_size = len(local_player.hand)
                card_pos = self.geometry.get_hand_card_pos(action.card_index, hand_size)
                self.highlight_signal.emit(card_pos)
                
                # Show card name
                card = local_player.hand[action.card_index]
                card_name = getattr(card.data, 'name', 'Card') if hasattr(card, 'data') and card.data else 'Card'
                self.status_signal.emit(f"PLAY: {card_name}")
                
        elif action.action_type == ActionType.HERO_POWER:
            hp_pos = self.geometry.get_hero_power_pos(is_opponent=False)
            self.highlight_signal.emit(hp_pos)
            
        elif action.action_type == ActionType.ATTACK:
            if action.attacker_index is not None and action.target_index is not None:
                # Get attacker position
                if action.attacker_index == -1:
                    # Hero is attacking
                    start_pos = self.geometry.get_hero_pos(is_opponent=False)
                elif action.attacker_index < len(local_player.board):
                    start_pos = self.geometry.get_player_minion_pos(
                        action.attacker_index, len(local_player.board)
                    )
                else:
                    return
                    
                # Get target position
                if action.target_index == -1:
                    # Face
                    end_pos = self.geometry.get_hero_pos(is_opponent=True)
                else:
                    opponent = self.game.players[1] if self.parser.local_player_id in [None, 1] else self.game.players[0]
                    if action.target_index < len(opponent.board):
                        end_pos = self.geometry.get_opponent_minion_pos(
                            action.target_index, len(opponent.board)
                        )
                    else:
                        end_pos = self.geometry.get_hero_pos(is_opponent=True)
                        
                self.arrow_signal.emit(start_pos, end_pos)

    def _suggest_heuristic(self, local_player):
        """Simple heuristic AI when no model is available."""
        # Priority 1: Play cards
        playable = [c for c in local_player.hand if hasattr(c, 'cost') and c.cost <= local_player.mana]
        
        if playable:
            # Play highest cost card first
            playable.sort(key=lambda c: c.cost, reverse=True)
            card = playable[0]
            card_name = getattr(card.data, 'name', 'Card') if hasattr(card, 'data') and card.data else 'Card'
            
            self.status_signal.emit(f"PLAY: {card_name}")
            self.info_signal.emit(f"Cost: {card.cost} | Mana: {local_player.mana}/{local_player.max_mana}")
            
            idx = local_player.hand.index(card)
            card_pos = self.geometry.get_hand_card_pos(idx, len(local_player.hand))
            self.highlight_signal.emit(card_pos)
            
            # Simple winrate based on board state
            my_board = sum(m.attack for m in local_player.board if hasattr(m, 'attack'))
            opp_board = sum(m.attack for m in self.game.players[1].board if hasattr(m, 'attack'))
            winrate = (my_board - opp_board) / 20  # Normalize to -1 to 1
            winrate = max(-1, min(1, winrate))
            self.winrate_signal.emit(winrate)
            return
            
        # Priority 2: Attack with minions
        can_attack = [m for m in local_player.board if hasattr(m, 'can_attack') and m.can_attack()]
        
        if can_attack:
            attacker = can_attack[0]
            attacker_idx = local_player.board.index(attacker)
            attacker_name = getattr(attacker.data, 'name', 'Minion') if hasattr(attacker, 'data') else 'Minion'
            
            # Check for taunts
            opponent = self.game.players[1]
            taunts = [m for m in opponent.board if hasattr(m, 'taunt') and m.taunt]
            
            if taunts:
                target = taunts[0]
                target_idx = opponent.board.index(target)
                target_name = getattr(target.data, 'name', 'Taunt') if hasattr(target, 'data') else 'Taunt'
                
                self.status_signal.emit(f"ATTACK: {attacker_name} → {target_name}")
                start_pos = self.geometry.get_player_minion_pos(attacker_idx, len(local_player.board))
                end_pos = self.geometry.get_opponent_minion_pos(target_idx, len(opponent.board))
            else:
                self.status_signal.emit(f"ATTACK: {attacker_name} → FACE")
                start_pos = self.geometry.get_player_minion_pos(attacker_idx, len(local_player.board))
                end_pos = self.geometry.get_hero_pos(is_opponent=True)
                
            self.info_signal.emit("Go face when possible!")
            self.arrow_signal.emit(start_pos, end_pos)
            return
            
        # Priority 3: End turn
        self.status_signal.emit("END TURN")
        self.info_signal.emit("No more actions available")
        self.arrow_signal.emit(None, None)
        self.highlight_signal.emit(None)


def main():
    app = QApplication(sys.argv)
    
    # Get screen geometry
    screen = QApplication.primaryScreen()
    if screen:
        screen_geo = screen.geometry()
        screen_width = screen_geo.width()
        screen_height = screen_geo.height()
    else:
        screen_width = 1920
        screen_height = 1080
    
    # Create overlay
    window = OverlayWindow()
    window.show()
    
    # Create worker
    worker = AssistantWorker(use_model=True)
    worker.geometry.resize(screen_width, screen_height)
    
    # Connect signals
    worker.status_signal.connect(window.update_status)
    worker.info_signal.connect(window.update_info)
    worker.winrate_signal.connect(window.update_winrate)
    worker.mana_signal.connect(window.update_mana)
    worker.arrow_signal.connect(window.set_arrow)
    worker.highlight_signal.connect(window.set_highlight)
    
    worker.start()
    
    print("[Assistant] Live Assistant started!")
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
