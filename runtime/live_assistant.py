"""
Live Assistant - Real-time Hearthstone AI Coach.
Watches game logs, analyzes state with AlphaZero, and displays suggestions via overlay.
"""

import sys
import os
import time
import threading
from typing import Optional

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
    action_queue_signal = pyqtSignal(list)  # List of (type, desc, details)
    
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
        self.use_model = False  # Disabled - model has fixed input size, real games have variable states
        self.brain = None
        # For now, always use heuristics until model architecture supports variable input
        print("[Assistant] Using heuristic-based suggestions (model disabled for live play)")
        
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
        refresh_counter = 0
        while self.running:
            time.sleep(0.5)
            refresh_counter += 1
            
            # Periodic analysis every ~2 seconds
            if refresh_counter % 4 == 0:
                self.think_and_suggest()
            
            # Also analyze when game state changes
            if self.parser.in_game:
                if time.time() - self.last_analysis_time > self.analysis_cooldown:
                    self.think_and_suggest()

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
            self.mana_signal.emit(local_player.mana, local_player.mana_crystals)
    
    def handle_log_line(self, line: str):
        """Called for every new log line."""
        state_changed = self.parser.parse_line(line)
        
        # Debug: check if lines are coming in
        # print(f"Log: {line.strip()}") 

        # Force update on specific events if parser missed them
        if "TAG_CHANGE" in line or "SHOW_ENTITY" in line or "BLOCK_START" in line:
            if time.time() - self.last_analysis_time > self.analysis_cooldown:
                self.think_and_suggest()

    def think_and_suggest(self):
        """AI Logic - Uses AlphaZero model if available."""
        self.last_analysis_time = time.time()
        
        # Note: With skip_history=True, in_game might not be set
        # We'll show suggestions regardless - user can ignore if not in game
        # if not self.parser.in_game:
        #     self.status_signal.emit("STANDBY")
        #     self.info_signal.emit("Waiting for game to start...")
        #     self.action_queue_signal.emit([])
        #     return
        
        # Skip mulligan check for now - detection is unreliable
        # TODO: Fix mulligan detection
        
        # For now, always show suggestions (user knows when it's their turn)
        # Turn detection will be improved later

        local_player = self.parser.get_local_player()
        if not local_player:
            self.status_signal.emit("ANALYZING...")
            self.info_signal.emit("Detecting players...")
            return
        
        # === MULLIGAN PHASE ===
        if self.parser.in_mulligan:
            self._suggest_mulligan(local_player)
            return
            
        # Update mana display
        self._update_mana()
        
        # Get perspective (1 = local player is P1, 2 = local player is P2)
        perspective = 1 if self.parser.local_player_id in [None, 1] else 2
        state = GameState.from_simulator_game(self.game, perspective_player_id=perspective)
        
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

    def _suggest_mulligan(self, local_player):
        """Suggest which cards to keep/mulligan using heuristics."""
        self.status_signal.emit("MULLIGAN")
        
        keep_cards = []
        mulligan_cards = []
        
        for i, card in enumerate(local_player.hand):
            card_name = "Unknown"
            card_cost = 99
            
            if hasattr(card, 'data') and card.data:
                card_name = getattr(card.data, 'name', 'Unknown')
            if hasattr(card, 'cost'):
                card_cost = card.cost
            
            # Heuristic: Keep cards with cost <= 3
            # Keep "The Coin" always
            should_keep = False
            if "coin" in card_name.lower():
                should_keep = True
            elif card_cost <= 3:
                should_keep = True
            
            if should_keep:
                keep_cards.append((i, card_name, card_cost))
            else:
                mulligan_cards.append((i, card_name, card_cost))
        
        # Build action queue for display
        actions = []
        for idx, name, cost in keep_cards:
            actions.append(("KEEP", f"Keep {name}", f"Cost: {cost} (Low)"))
        for idx, name, cost in mulligan_cards:
            actions.append(("MULLIGAN", f"Mulligan {name}", f"Cost: {cost} (Too high)"))
        
        self.action_queue_signal.emit(actions)
        
        # Update info
        keep_count = len(keep_cards)
        mulligan_count = len(mulligan_cards)
        self.info_signal.emit(f"Keep {keep_count}, Mulligan {mulligan_count}")
        
        # Highlight first card to mulligan (if any)
        if mulligan_cards:
            first_mulligan_idx = mulligan_cards[0][0]
            hand_size = len(local_player.hand)
            card_pos = self.geometry.get_hand_card_pos(first_mulligan_idx, hand_size)
            self.highlight_signal.emit(card_pos)
        else:
            self.highlight_signal.emit(None)
            
        print(f"[MULLIGAN] Keep: {[k[1] for k in keep_cards]}, Mulligan: {[m[1] for m in mulligan_cards]}")

    def _suggest_heuristic(self, local_player):
        """Build a full turn plan using simple heuristics."""
        actions = []
        # Trust parsed mana, but fallback if crystals are 0 (parser not ready)
        current_mana = local_player.mana
        if local_player.mana_crystals == 0:
             current_mana = 10 
        
        # DEBUG: Show BOTH players' hands and boards
        for i, p in enumerate(self.game.players):
            hand_cards = [(getattr(c.data, 'name', 'Unknown') if hasattr(c, 'data') and c.data else 'Unknown', 
                           getattr(c, 'cost', '?')) for c in p.hand]
            board_cards = [(getattr(m.data, 'name', 'Unknown'), getattr(m, 'atk', getattr(m, 'attack', 0)), getattr(m, 'health', 0)) for m in p.board]
            print(f"[DEBUG] Player {i}: Hand({len(p.hand)})={hand_cards[:3]}... Board({len(p.board)})={board_cards} Mana={p.mana}/{p.mana_crystals}")
        
        print(f"[HEURISTIC] Using local_player_id={self.parser.local_player_id}")
        
        # Copy hand for simulation
        simulated_hand = list(local_player.hand)
        
        
        # 1. Play cards (Greedy: most expensive first)
        # Filter playable cards
        playable_indices = []
        for i, card in enumerate(simulated_hand):
            if hasattr(card, 'cost'):
                playable_indices.append(i)
        
        # Sort by cost descending
        playable_indices.sort(key=lambda i: simulated_hand[i].cost, reverse=True)
        
        for i in playable_indices:
            card = simulated_hand[i]
            if card.cost <= current_mana:
                card_name = getattr(card.data, 'name', 'Card') if hasattr(card, 'data') and card.data else 'Card'
                
                # Add to queue
                actions.append((
                    "PLAY", 
                    f"Play {card_name}", 
                    f"Hand position: {i+1} | Cost: {card.cost}"
                ))
                
                # Simulate mana cost
                current_mana -= card.cost
                
                # Highlight first card to play
                if len(actions) == 1:
                     hand_size = len(local_player.hand)
                     card_pos = self.geometry.get_hand_card_pos(i, hand_size)
                     self.highlight_signal.emit(card_pos)
                     self.status_signal.emit(f"PLAY {card_name}")

        # 2. Attack with minions on board
        # Note: only take those ALREADY on board (not ones we just suggested to play)
        # Parser must be accurate on board state.
        for i, minion in enumerate(local_player.board):
            # Basic check (exhausted is often updated by logs)
            can_attack = True
            if hasattr(minion, 'exhausted') and minion.exhausted:
                can_attack = False
            if hasattr(minion, 'frozen') and minion.frozen:
                can_attack = False
            if hasattr(minion, 'can_attack') and not minion.can_attack(): # If method available
                can_attack = False
            
            if can_attack:
                m_name = getattr(minion.data, 'name', 'Minion') if hasattr(minion, 'data') else 'Minion'
                
                # Find taunt target (simulation)
                target_desc = "Face"
                opponent = self.game.players[1] if self.parser.local_player_id in [None, 1] else self.game.players[0]
                taunts = [m for m in opponent.board if hasattr(m, 'taunt') and m.taunt]
                
                if taunts:
                    t_name = getattr(taunts[0].data, 'name', 'Taunt') if hasattr(taunts[0].data, 'data') else 'Taunt'
                    target_desc = f"{t_name}"
                
                actions.append((
                    "ATTACK",
                    f"Attack with {m_name}",
                    f"Target: {target_desc} (Position {i+1})"
                ))
                
                # If first action (no cards played before), show arrow
                if len(actions) == 1:
                     start_pos = self.geometry.get_player_minion_pos(i, len(local_player.board))
                     if taunts:
                         end_pos = self.geometry.get_opponent_minion_pos(0, len(opponent.board)) # First taunt
                     else:
                         end_pos = self.geometry.get_hero_pos(is_opponent=True)
                     self.arrow_signal.emit(start_pos, end_pos)

        # 3. End turn
        actions.append(("END", "End Turn", "Pass the turn"))
        if len(actions) == 1: # Only end turn
             self.status_signal.emit("END TURN")
             self.arrow_signal.emit(None, None)
             self.highlight_signal.emit(None)

        # DEBUG: Print found actions
        print(f"[HEURISTIC] ACTIONS FOUND ({len(actions)}):")
        for a in actions:
            print(f"  - {a}")

        # Send full queue
        self.action_queue_signal.emit(actions)
        
        # Basic winrate
        my_stats = sum(m.attack + m.health for m in local_player.board if hasattr(m, 'attack'))
        opp_stats = sum(m.attack + m.health for m in self.game.players[1].board if hasattr(m, 'attack'))
        base_wr = 0.5 + (my_stats - opp_stats) * 0.02
        self.winrate_signal.emit(max(0.1, min(0.9, base_wr)))


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
    worker.action_queue_signal.connect(window.set_action_queue) # Nouvelle connexion
    
    worker.start()
    
    print("[Assistant] Live Assistant started!")
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
