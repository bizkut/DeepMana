"""
Log Parser for Hearthstone Power.log.
Converts raw log lines into Game State updates for the Simulator.
Enhanced with player detection, hero tracking, and attack detection.
"""

import re
from typing import Optional, Dict, List, Callable
from simulator.game import Game
from simulator.player import Player
from simulator.card_loader import CardDatabase
from simulator.enums import Zone
from simulator.factory import create_card

class LogParser:
    def __init__(self, game: Game, on_state_change: Optional[Callable] = None):
        self.game = game
        self.entity_map: Dict[int, object] = {}  # ID -> Entity
        self.on_state_change = on_state_change
        
        # Player Detection
        self.local_player_id: Optional[int] = None  # 1 or 2
        self.local_player_name: Optional[str] = None
        
        # Hero Tracking
        self.hero_entities: Dict[int, int] = {}  # player_id -> hero_entity_id
        
        # Game Phase
        self.in_game = False
        self.mulligan_complete = False
        
        # Regex Patterns
        self.regex_tag = re.compile(r"TAG_CHANGE Entity=(.*?) tag=(.*?) value=(.*)")
        self.regex_entity_block = re.compile(r"\[id=(\d+)(?: cardId=(\S+))?(?: name=([^\]]+))?\]")
        self.regex_block_start = re.compile(r"BLOCK_START.*BlockType=(\w+).*Entity=\[.*id=(\d+)")
        self.regex_block_end = re.compile(r"BLOCK_END")
        self.regex_player_entity = re.compile(r"PlayerID=(\d+), PlayerName=(.*)")
        self.regex_show_entity = re.compile(r"SHOW_ENTITY.*\[.*id=(\d+).*cardId=(\S+)")
        self.regex_hide_entity = re.compile(r"HIDE_ENTITY.*\[.*id=(\d+)")
        self.regex_attack = re.compile(r"BLOCK_START.*BlockType=ATTACK.*Entity=\[.*id=(\d+).*\].*Target=\[.*id=(\d+)")
        
        # Track current block for context
        self.current_block = None
        
    def parse_line(self, line: str) -> bool:
        """Parse a single log line. Returns True if state changed."""
        line = line.strip()
        
        # Filter non-power lines
        if "DebugPrintPower" not in line and "PowerTaskList" not in line:
            return False

        state_changed = False
        
        # === GAME START DETECTION ===
        if "CREATE_GAME" in line:
            self.in_game = True
            self._reset_game_state()
            state_changed = True
            
        # === PLAYER DETECTION ===
        player_match = self.regex_player_entity.search(line)
        if player_match:
            player_id = int(player_match.group(1))
            player_name = player_match.group(2)
            
            # Update game players
            if player_id <= len(self.game.players):
                self.game.players[player_id - 1].name = player_name
            
        # === LOCAL PLAYER DETECTION ===
        # The first CURRENT_PLAYER=1 after CREATE_GAME is usually the local player
        if "tag=MULLIGAN_STATE" in line and "value=INPUT" in line:
            # This player is in mulligan -> they are deciding -> likely local
            entity_match = re.search(r"Entity=\[.*player=(\d+)", line)
            if entity_match:
                self.local_player_id = int(entity_match.group(1))
        
        # === TAG CHANGES ===
        tag_match = self.regex_tag.search(line)
        if tag_match:
            entity_str = tag_match.group(1)
            tag = tag_match.group(2)
            value = tag_match.group(3)
            if self._handle_tag_change(entity_str, tag, value):
                state_changed = True
        
        # === FULL_ENTITY (Card Creation) ===
        if "FULL_ENTITY" in line:
            if self._handle_full_entity(line):
                state_changed = True
        
        # === SHOW_ENTITY (Card Reveal) ===
        show_match = self.regex_show_entity.search(line)
        if show_match:
            entity_id = int(show_match.group(1))
            card_id = show_match.group(2)
            self._handle_show_entity(entity_id, card_id)
            state_changed = True
            
        # === ATTACK DETECTION ===
        attack_match = self.regex_attack.search(line)
        if attack_match:
            attacker_id = int(attack_match.group(1))
            target_id = int(attack_match.group(2))
            self._handle_attack(attacker_id, target_id)
            state_changed = True
            
        # === BLOCK TRACKING (for context) ===
        block_start = self.regex_block_start.search(line)
        if block_start:
            self.current_block = {
                'type': block_start.group(1),
                'entity_id': int(block_start.group(2))
            }
            
        if self.regex_block_end.search(line):
            self.current_block = None
            
        # Notify if state changed
        if state_changed and self.on_state_change:
            self.on_state_change()
            
        return state_changed

    def _reset_game_state(self):
        """Reset game state for new game."""
        self.entity_map.clear()
        self.hero_entities.clear()
        self.local_player_id = None
        self.mulligan_complete = False
        
        for p in self.game.players:
            p.hand.clear()
            p.board.clear()
            p.graveyard.clear()
            p.deck.clear()
            p.mana = 0
            p.max_mana = 0
            p.hero = None
            p.hero_power = None
            
    def _handle_full_entity(self, line: str) -> bool:
        """Handles FULL_ENTITY lines (card creation)."""
        entity_data = self._parse_entity_str(line)
        if not entity_data or entity_data.get('id', -1) == -1:
            return False
        
        entity_id = entity_data['id']
        
        # Only create if we have a cardId
        if entity_data.get('cardId'):
            card_id = entity_data['cardId']
            
            # Check if this is a Hero card
            if 'HERO' in card_id.upper():
                player_id = entity_data.get('player', 1)
                self.hero_entities[player_id] = entity_id
            
            entity = self._get_or_create_entity(entity_id, entity_data)
            if entity:
                # Determine zone from the line if present
                zone_match = re.search(r'zone=(\w+)', line)
                if zone_match:
                    zone_str = zone_match.group(1)
                    try:
                        new_zone = Zone[zone_str]
                        self._move_to_zone(entity, new_zone)
                        return True
                    except KeyError:
                        pass
        return False

    def _handle_show_entity(self, entity_id: int, card_id: str):
        """Handle revealed cards (opponent's cards becoming known)."""
        if entity_id in self.entity_map:
            entity = self.entity_map[entity_id]
            # Update the card's identity
            if hasattr(entity, 'card_id'):
                entity.card_id = card_id
                # Load card data
                card_data = CardDatabase.get_card(card_id)
                if card_data:
                    entity.data = card_data
                    
    def _handle_attack(self, attacker_id: int, target_id: int):
        """Track attack events for visualization."""
        # This can be used to trigger arrow display
        pass  # The overlay handles this through the brain suggestions
        
    def _handle_tag_change(self, entity_str: str, tag: str, value: str) -> bool:
        entity_data = self._parse_entity_str(entity_str)
        if not entity_data:
            return False
            
        entity_id = entity_data.get('id', -1)
        state_changed = False
        
        # === ZONE CHANGES ===
        if tag == "ZONE":
            if entity_id != -1:
                state_changed = self._handle_zone_change(entity_id, value, entity_data)
                
        # === STATS UPDATES ===
        elif tag == "DAMAGE":
            if entity_id != -1:
                entity = self._get_or_create_entity(entity_id, entity_data)
                if entity and hasattr(entity, 'damage'):
                    entity.damage = int(value)
                    state_changed = True
                    
        elif tag == "ATK":
            if entity_id != -1:
                entity = self._get_or_create_entity(entity_id, entity_data)
                if entity and hasattr(entity, 'attack'):
                    try:
                        entity.attack = int(value)
                        state_changed = True
                    except ValueError:
                        pass
                        
        elif tag == "HEALTH":
            if entity_id != -1:
                entity = self._get_or_create_entity(entity_id, entity_data)
                if entity and hasattr(entity, 'health'):
                    try:
                        entity.health = int(value)
                        state_changed = True
                    except ValueError:
                        pass
                        
        elif tag == "ARMOR":
            if entity_id != -1:
                entity = self._get_or_create_entity(entity_id, entity_data)
                if entity and hasattr(entity, 'armor'):
                    try:
                        entity.armor = int(value)
                        state_changed = True
                    except ValueError:
                        pass
                        
        # === MANA ===
        elif tag == "RESOURCES":
            player_name = entity_data.get('name')
            try:
                mana_value = int(value)
                for p in self.game.players:
                    if p.name == player_name:
                        p.max_mana = mana_value
                        state_changed = True
                        break
            except ValueError:
                pass
                
        elif tag == "RESOURCES_USED":
            player_name = entity_data.get('name')
            try:
                used = int(value)
                for p in self.game.players:
                    if p.name == player_name:
                        p.mana = p.max_mana - used
                        state_changed = True
                        break
            except ValueError:
                pass
                
        # === CURRENT PLAYER ===
        elif tag == "CURRENT_PLAYER":
            if value == "1":
                player_name = entity_data.get('name')
                if player_name:
                    for idx, p in enumerate(self.game.players):
                        if p.name == player_name:
                            self.game.current_player_idx = idx
                            state_changed = True
                            break
                            
        # === GAME END ===
        elif tag == "PLAYSTATE":
            if value in ["WON", "LOST", "TIED"]:
                self.in_game = False
                state_changed = True
                
        # === KEYWORDS ===
        elif tag in ["TAUNT", "DIVINE_SHIELD", "STEALTH", "FROZEN", "WINDFURY", 
                     "CHARGE", "RUSH", "IMMUNE", "POISONOUS", "LIFESTEAL", "REBORN"]:
            if entity_id != -1:
                entity = self._get_or_create_entity(entity_id, entity_data)
                if entity:
                    setattr(entity, tag.lower(), value == "1")
                    
        elif tag == "EXHAUSTED":
            if entity_id != -1:
                entity = self._get_or_create_entity(entity_id, entity_data)
                if entity:
                    entity.exhausted = (value == "1")
                    
        elif tag == "CONTROLLER":
            if entity_id != -1:
                entity = self._get_or_create_entity(entity_id, entity_data)
                if entity:
                    try:
                        new_idx = int(value) - 1
                        if 0 <= new_idx < len(self.game.players):
                            self._change_controller(entity, self.game.players[new_idx])
                            state_changed = True
                    except ValueError:
                        pass
                        
        return state_changed
            
    def _parse_entity_str(self, entity_str: str) -> Optional[dict]:
        """Parses [entityName=... id=X ... cardId=Y player=Z] or plain name."""
        bracket_match = re.search(r'\[([^\]]+)\]', entity_str)
        if bracket_match:
            content = bracket_match.group(1)
            result = {}
            
            id_match = re.search(r'id=(\d+)', content)
            if id_match: result['id'] = int(id_match.group(1))
            else: result['id'] = -1
            
            cardId_match = re.search(r'cardId=(\S+)', content)
            if cardId_match: result['cardId'] = cardId_match.group(1)
            
            name_match = re.search(r'entityName=([^\s\]]+)', content)
            if name_match: result['name'] = name_match.group(1)
            
            player_match = re.search(r'player=(\d+)', content)
            if player_match: result['player'] = int(player_match.group(1))
            
            zonePos_match = re.search(r'zonePos=(\d+)', content)
            if zonePos_match: result['zonePos'] = int(zonePos_match.group(1))
            
            return result
        
        return {'id': -1, 'name': entity_str}

    def _handle_zone_change(self, entity_id: int, zone_value: str, entity_data: dict) -> bool:
        """Moves card between zones."""
        try:
            new_zone = Zone[zone_value]
        except KeyError:
            return False
            
        entity = self._get_or_create_entity(entity_id, entity_data)
        if not entity:
            return False
            
        return self._move_to_zone(entity, new_zone)

    def _move_to_zone(self, entity, new_zone: Zone) -> bool:
        """Move entity to a new zone."""
        if not hasattr(entity, 'zone') or not hasattr(entity, 'controller'):
            return False
            
        old_zone = entity.zone
        if old_zone == new_zone:
            return False
            
        controller = entity.controller
        
        # Remove from old zone
        if old_zone == Zone.HAND and entity in controller.hand:
            controller.hand.remove(entity)
        elif old_zone == Zone.PLAY and entity in controller.board:
            controller.board.remove(entity)
        elif old_zone == Zone.GRAVEYARD and entity in controller.graveyard:
            controller.graveyard.remove(entity)
        elif old_zone == Zone.SECRET and hasattr(controller, 'secrets') and entity in controller.secrets:
            controller.secrets.remove(entity)
            
        # Add to new zone
        entity.zone = new_zone
        if new_zone == Zone.HAND:
            controller.hand.append(entity)
        elif new_zone == Zone.PLAY:
            controller.board.append(entity)
        elif new_zone == Zone.GRAVEYARD:
            controller.graveyard.append(entity)
        elif new_zone == Zone.SECRET:
            if not hasattr(controller, 'secrets'):
                controller.secrets = []
            controller.secrets.append(entity)
            
        return True

    def _change_controller(self, entity, new_controller):
        """Moves entity to new controller."""
        old_controller = entity.controller
        if old_controller == new_controller:
            return

        if old_controller:
            if entity in old_controller.hand: old_controller.hand.remove(entity)
            elif entity in old_controller.board: old_controller.board.remove(entity)
            elif entity in old_controller.graveyard: old_controller.graveyard.remove(entity)
        
        entity.controller = new_controller
        
        if entity.zone == Zone.HAND: new_controller.hand.append(entity)
        elif entity.zone == Zone.PLAY: new_controller.board.append(entity)
        elif entity.zone == Zone.GRAVEYARD: new_controller.graveyard.append(entity)
                
    def _get_or_create_entity(self, entity_id: int, data: dict):
        if entity_id in self.entity_map:
            return self.entity_map[entity_id]
            
        if data.get('cardId'):
            card_id = data['cardId']
            controller_idx = data.get('player', 1) - 1
            if 0 <= controller_idx < len(self.game.players):
                controller = self.game.players[controller_idx]
            else:
                controller = self.game.players[0]
            
            new_entity = create_card(card_id, controller)
            if new_entity:
                new_entity.entity_id = entity_id
                
                if 'zonePos' in data:
                    new_entity.zone_position = data['zonePos']
                
                self.entity_map[entity_id] = new_entity
                return new_entity
            
        return None
    
    def is_local_player_turn(self) -> bool:
        """Check if it's the local player's turn."""
        if self.local_player_id is None:
            return self.game.current_player_idx == 0
        return self.game.current_player_idx == self.local_player_id - 1
    
    def get_local_player(self) -> Optional[Player]:
        """Get the local player object."""
        if self.local_player_id is None:
            return self.game.players[0] if self.game.players else None
        idx = self.local_player_id - 1
        if 0 <= idx < len(self.game.players):
            return self.game.players[idx]
        return None
