"""
Log Parser for Hearthstone Power.log.
Converts raw log lines into Game State updates for the Simulator.
"""

import re
from typing import Optional, Dict, List
from simulator.game import Game
from simulator.player import Player
from simulator.card_loader import CardDatabase

from simulator.enums import Zone
from simulator.factory import create_card

class LogParser:
    def __init__(self, game: Game):
        self.game = game
        self.entity_map: Dict[int, object] = {} # ID -> Entity (Player/Card/Hero)
        
        # Regex (Existing...)
        self.regex_tag = re.compile(r"TAG_CHANGE Entity=(.*?) tag=(.*?) value=(.*)")
        self.regex_entity_block = re.compile(r"\[id=(\d+)(?: cardId=(.*?))?(?: name=(.*?))?\]")
        
    def parse_line(self, line: str):
        # (Existing logic...)
        line = line.strip()
        if "DebugPrintPower" not in line and "PowerTaskList" not in line:
            return

        # Check for TAG_CHANGE
        tag_match = self.regex_tag.search(line)
        if tag_match:
            entity_str = tag_match.group(1)
            tag = tag_match.group(2)
            value = tag_match.group(3)
            self._handle_tag_change(entity_str, tag, value)
            return
        
        # Check for FULL_ENTITY (card creation)
        if "FULL_ENTITY" in line:
            self._handle_full_entity(line)

    def _handle_full_entity(self, line: str):
        """Handles FULL_ENTITY lines (card creation)."""
        entity_data = self._parse_entity_str(line)
        if not entity_data or entity_data.get('id', -1) == -1:
            return
        
        entity_id = entity_data['id']
        
        # Only create if we have a cardId
        if entity_data.get('cardId'):
            entity = self._get_or_create_entity(entity_id, entity_data)
            if entity:
                # Determine zone from the line if present
                zone_match = re.search(r'zone=(\w+)', line)
                if zone_match:
                    zone_str = zone_match.group(1)
                    try:
                        from simulator.enums import Zone
                        new_zone = Zone[zone_str]
                        entity.zone = new_zone
                        
                        # Add to appropriate list
                        if new_zone == Zone.HAND and entity not in entity.controller.hand:
                            entity.controller.hand.append(entity)
                        elif new_zone == Zone.PLAY and entity not in entity.controller.board:
                            entity.controller.board.append(entity)
                        elif new_zone == Zone.DECK:
                            pass  # Deck tracking not implemented
                    except KeyError:
                        pass

    def _handle_tag_change(self, entity_str: str, tag: str, value: str):
        entity_data = self._parse_entity_str(entity_str)
        if not entity_data:
            return
            
        entity_id = entity_data['id']
        
        if tag == "ZONE":
            self._handle_zone_change(entity_id, value, entity_data)
        elif tag == "DAMAGE":
            if entity_id != -1:
                entity = self._get_or_create_entity(entity_id, entity_data)
                if entity and hasattr(entity, 'damage'):
                    entity.damage = int(value)
        elif tag == "CONTROLLER":
            if entity_id != -1:
                entity = self._get_or_create_entity(entity_id, entity_data)
                if entity and hasattr(entity, 'controller'):
                    # Value 1 -> Player 0, Value 2 -> Player 1
                    try:
                        new_controller_idx = int(value) - 1
                        if 0 <= new_controller_idx < len(self.game.players):
                            new_controller = self.game.players[new_controller_idx]
                            self._change_controller(entity, new_controller)
                    except ValueError:
                        pass

        elif tag == "CURRENT_PLAYER":
            if value == "1":
                # Find player with this name
                player_name = entity_data.get('name')
                if player_name:
                    for idx, p in enumerate(self.game.players):
                        if p.name == player_name:
                            self.game.current_player_idx = idx
                            break
            
    def _parse_entity_str(self, entity_str: str) -> Optional[dict]:
        """Parses [entityName=... id=X ... cardId=Y player=Z] or plain name."""
        # Try to match bracketed entity format
        bracket_match = re.search(r'\[([^\]]+)\]', entity_str)
        if bracket_match:
            content = bracket_match.group(1)
            result = {}
            
            # Extract id (required for cards)
            id_match = re.search(r'id=(\d+)', content)
            if id_match: result['id'] = int(id_match.group(1))
            else: result['id'] = -1
            
            # Extract cardId (identifies the card type)
            cardId_match = re.search(r'cardId=(\S+)', content)
            if cardId_match and cardId_match.group(1):
                result['cardId'] = cardId_match.group(1)
            
            # Extract entityName
            name_match = re.search(r'entityName=([^\s\]]+)', content)
            if name_match: result['name'] = name_match.group(1)
            
            # Extract player (controller ID, 1 or 2)
            player_match = re.search(r'player=(\d+)', content)
            if player_match: result['player'] = int(player_match.group(1))
            
            # Extract zonePos (position in zone, 1-indexed)
            zonePos_match = re.search(r'zonePos=(\d+)', content)
            if zonePos_match: result['zonePos'] = int(zonePos_match.group(1))
            
            return result
        
        # Fallback: Plain string (e.g. "Kevzi" or "GameEntity")
        return {'id': -1, 'name': entity_str}

    def _handle_zone_change(self, entity_id: int, zone_value: str, entity_data: dict):
        """Moves card between zones."""
        # Clean zone value (e.g. "HAND" -> Zone.HAND)
        try:
            new_zone = Zone[zone_value]
        except KeyError:
            return # Unknown zone
            
        # Get Simulator Entity
        entity = self._get_or_create_entity(entity_id, entity_data)
        if not entity:
            return

        # Update Simulator State
        # If it's a Card, move it
        if hasattr(entity, 'zone'):
            # Remove from old zone
            if entity.zone == Zone.HAND and entity in entity.controller.hand:
                entity.controller.hand.remove(entity)
            elif entity.zone == Zone.PLAY and entity in entity.controller.board:
                entity.controller.board.remove(entity)
            elif entity.zone == Zone.DECK:
                 pass 
            elif entity.zone == Zone.GRAVEYARD and entity in entity.controller.graveyard:
                entity.controller.graveyard.remove(entity)
            elif entity.zone == Zone.SETASIDE and entity in entity.controller.setaside:
                entity.controller.setaside.remove(entity)
            elif entity.zone == Zone.SECRET and entity in entity.controller.secrets:
                entity.controller.secrets.remove(entity)
            
            # Add to new zone
            entity.zone = new_zone
            if new_zone == Zone.HAND:
                entity.controller.hand.append(entity)
            elif new_zone == Zone.PLAY:
                entity.controller.board.append(entity)
            elif new_zone == Zone.GRAVEYARD:
                entity.controller.graveyard.append(entity)
            elif new_zone == Zone.SETASIDE:
                entity.controller.setaside.append(entity)
            elif new_zone == Zone.SECRET:
                entity.controller.secrets.append(entity)

    def _change_controller(self, entity, new_controller):
        """Moves entity to new controller."""
        old_controller = entity.controller
        if old_controller == new_controller:
            return

        if old_controller:
            if entity in old_controller.hand: old_controller.hand.remove(entity)
            elif entity in old_controller.board: old_controller.board.remove(entity)
            elif entity in old_controller.graveyard: old_controller.graveyard.remove(entity)
            elif entity in old_controller.setaside: old_controller.setaside.remove(entity)
        
        entity.controller = new_controller
        
        if entity.zone == Zone.HAND: new_controller.hand.append(entity)
        elif entity.zone == Zone.PLAY: new_controller.board.append(entity)
        elif entity.zone == Zone.GRAVEYARD: new_controller.graveyard.append(entity)
        elif entity.zone == Zone.SETASIDE: new_controller.setaside.append(entity)
                
    def _get_or_create_entity(self, entity_id: int, data: dict):
        if entity_id in self.entity_map:
            return self.entity_map[entity_id]
            
        # Create new card entity
        if data.get('cardId'):
            card_id = data['cardId']
            
            # Determine controller from 'player' field (1-indexed in logs)
            controller_idx = data.get('player', 1) - 1  # Default to player 1 (index 0)
            if 0 <= controller_idx < len(self.game.players):
                controller = self.game.players[controller_idx]
            else:
                controller = self.game.players[0]
            
            new_entity = create_card(card_id, controller)
            new_entity.entity_id = entity_id
            
            # Store zone position if available
            if 'zonePos' in data:
                new_entity.zone_position = data['zonePos']
            
            self.entity_map[entity_id] = new_entity
            return new_entity
            
        return None
