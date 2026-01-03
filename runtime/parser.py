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

        tag_match = self.regex_tag.search(line)
        if tag_match:
            entity_str = tag_match.group(1)
            tag = tag_match.group(2)
            value = tag_match.group(3)
            self._handle_tag_change(entity_str, tag, value)

    def _handle_tag_change(self, entity_str: str, tag: str, value: str):
        entity_data = self._parse_entity_str(entity_str)
        if not entity_data:
            return
            
        entity_id = entity_data['id']
        
        if tag == "ZONE":
            self._handle_zone_change(entity_id, value, entity_data)
        elif tag == "DAMAGE":
            # For damage log, we expect a valid ID usually
            if entity_id != -1:
                entity = self._get_or_create_entity(entity_id, entity_data)
                if entity and hasattr(entity, 'damage'):
                    entity.damage = int(value)
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
        """Parses [id=1 cardId=...] block or returns Name dict."""
        match = self.regex_entity_block.search(entity_str)
        if match:
            return {
                'id': int(match.group(1)),
                'cardId': match.group(2),
                'name': match.group(3)
            }
        # Fallback: Plain string (e.g. "Player 2")
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
                
    def _get_or_create_entity(self, entity_id: int, data: dict):
        if entity_id in self.entity_map:
            return self.entity_map[entity_id]
            
        # Create new
        if data.get('cardId'):
            # It's a card/hero/power
            card_id = data['cardId']
            # Determine controller (placeholder logic)
            # Logs usually imply controller via logs, but here we guess/default to P1
            # Ideally we check the CONTROLLER tag.
            controller = self.game.players[0] 
            
            new_entity = create_card(card_id, controller)
            new_entity.entity_id = entity_id # Sync ID
            self.entity_map[entity_id] = new_entity
            return new_entity
            
        return None
