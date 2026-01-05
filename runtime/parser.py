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
        
        # Entity tracking for inline tags
        self.last_entity_id: Optional[int] = None
        
        # Game Phase
        self.in_game = False
        self.in_mulligan = False  # True during mulligan card selection
        self.mulligan_complete = False
        self.current_player_id: Optional[int] = None  # 1 or 2 (whose turn)
        
        # Regex Patterns
        self.regex_tag = re.compile(r"TAG_CHANGE Entity=(.*?) tag=(.*?) value=(.*)")
        self.regex_entity_block = re.compile(r"\[id=(\d+)(?: cardId=(\S+))?(?: name=([^\]]+))?\]")
        self.regex_block_start = re.compile(r"BLOCK_START.*BlockType=(\w+).*Entity=\[.*id=(\d+)")
        self.regex_block_end = re.compile(r"BLOCK_END")
        self.regex_player_entity = re.compile(r"PlayerID=(\d+), PlayerName=(.*)")
        # SHOW_ENTITY has two formats:
        # 1. Simple: SHOW_ENTITY - Updating Entity=28 CardID=VAC_408
        # 2. Bracket: SHOW_ENTITY - Updating Entity=[...id=28...] CardID=VAC_408
        self.regex_show_entity = re.compile(r"SHOW_ENTITY.*Entity=(?:\[.*?id=)?(\d+).*?CardID=(\S+)")
        self.regex_hide_entity = re.compile(r"HIDE_ENTITY.*\[.*id=(\d+)")
        self.regex_attack = re.compile(r"BLOCK_START.*BlockType=ATTACK.*Entity=\[.*id=(\d+).*\].*Target=\[.*id=(\d+)")
        
        # Track current block for context
        self.current_block = None
        
    def _resolve_player_name(self, name_str: str) -> Optional[Player]:
        """
        Dynamically bind a name to a player if not already known.
        Useful when joining mid-game (history skipped) and we see 'TAG_CHANGE Entity=Name'.
        """
        # 0. Safety: Ignore known non-player entities
        if name_str in ["GameEntity", "The Coin", "UNKNOWN ENTITY"]:
             return None
             
        # 1. Check if we already know this name
        for p in self.game.players:
            if p.name == name_str:
                return p
                
        # 2. Check if we can bind it to a default player
        # We need a robust way to decide if this is P1 or P2.
        # But if we have NO info, first come first served is better than nothing.
        # Player 1 is usually the local player in many contexts, or at least the first initialized.
        
        # Bind to Player 1 if it's "Player 1" (default)
        if self.game.players[0].name == "Player 1":
            print(f"[Parser] Binding unknown name '{name_str}' to Player 1")
            self.game.players[0].name = name_str
            return self.game.players[0]
            
        # Bind to Player 2 if it's "Opponent" (default)
        if len(self.game.players) > 1 and self.game.players[1].name == "Opponent":
            print(f"[Parser] Binding unknown name '{name_str}' to Player 2")
            self.game.players[1].name = name_str
            return self.game.players[1]
            
        return None

    def parse_line(self, line: str) -> bool:
        """Parse a single log line. Returns True if state changed."""
        line = line.strip()
        
        # Filter non-power lines
        # Allow DebugPrintPower, PowerTaskList, and DebugPrintGame (for player names)
        if "DebugPrintPower" not in line and "PowerTaskList" not in line and "DebugPrintGame" not in line:
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
            
        # === LOCAL PLAYER DETECTION + MULLIGAN STATE ===
        # The first CURRENT_PLAYER=1 after CREATE_GAME is usually the local player
        if "tag=MULLIGAN_STATE" in line and "value=INPUT" in line:
            # Player is in mulligan -> they are deciding cards
            self.in_mulligan = True
            entity_match = re.search(r"Entity=\[.*player=(\d+)", line)
            if entity_match:
                self.local_player_id = int(entity_match.group(1))
            elif self.local_player_id is None:
                # Fallback: first player to enter mulligan is likely local
                # Try alternative format: Entity=PlayerName 
                name_match = re.search(r"Entity=([^\s\[]+)", line)
                if name_match:
                    player_name = name_match.group(1)
                    # Find which player has this name
                    for i, p in enumerate(self.game.players):
                        if p.name == player_name:
                            self.local_player_id = i + 1
                            break
                if self.local_player_id is None:
                    self.local_player_id = 1  # Default to player 1
        
        # === TAG CHANGES ===
        tag_match = self.regex_tag.search(line)
        if tag_match:
            entity_str = tag_match.group(1)
            tag = tag_match.group(2)
            value = tag_match.group(3)
            

            if self._handle_tag_change(entity_str, tag, value):
                state_changed = True
        
        # === INLINE TAGS (after FULL_ENTITY) ===
        # These are lines like: "D ... PowerTaskList.DebugPrintPower() -         tag=ZONE value=DECK"
        # They have "tag=X value=Y" but are NOT TAG_CHANGE lines
        # Check: has "tag=" AND "value=" but NOT "TAG_CHANGE" and NOT "Entity="
        if "tag=" in line and "value=" in line and "TAG_CHANGE" not in line and "Entity=" not in line:
            inline_tag_match = re.search(r'tag=(\w+)\s+value=(\w+)', line)
            if inline_tag_match and self.last_entity_id:
                tag = inline_tag_match.group(1)
                value = inline_tag_match.group(2)
                
                if tag == "ZONE":
                    try:
                        new_zone = Zone[value]
                        if self.last_entity_id in self.entity_map:
                            entity = self.entity_map[self.last_entity_id]
                            self._move_to_zone(entity, new_zone)
                            state_changed = True
                    except KeyError:
                        pass
        
        # Clear last_entity_id when we see a new major line (FULL_ENTITY, TAG_CHANGE, etc)
        if "TAG_CHANGE" in line or "BLOCK_START" in line or "BLOCK_END" in line:
            self.last_entity_id = None
        
        # === FULL_ENTITY (Card Creation) ===
        if "FULL_ENTITY" in line:
            if self._handle_full_entity(line):
                state_changed = True
        
        # === SHOW_ENTITY (Card Reveal) ===
        show_match = self.regex_show_entity.search(line)
        if show_match:
            entity_id = int(show_match.group(1))
            card_id = show_match.group(2)
            
            # Track for inline tags
            self.last_entity_id = entity_id
            
            # Handle the reveal
            self._handle_show_entity(entity_id, card_id, line)
            # Check zone using entity map
            zone = "Unknown"
            if entity_id in self.entity_map:
                ent = self.entity_map[entity_id]
                if hasattr(ent, 'tags'):
                    zone = ent.tags.get('ZONE', 'Unknown')
                
            print(f"[SHOW_ENTITY] id={entity_id} cardId={card_id} Zone={zone} (in map: {entity_id in self.entity_map})")
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
        self.in_mulligan = False
        self.mulligan_complete = False
        self.current_player_id = None
        
        for p in self.game.players:
            p.hand.clear()
            p.board.clear()
            p.graveyard.clear()
            p.deck.clear()
            p.mana = 0
            p.mana_crystals = 0
            p.hero = None
            
    def _handle_full_entity(self, line: str) -> bool:
        """Handles FULL_ENTITY lines (card creation)."""
        entity_data = self._parse_entity_str(line)
        if not entity_data or entity_data.get('id', -1) == -1:
            return False
        
        entity_id = entity_data['id']
        card_id = entity_data.get('cardId', '')
        
        # Track for inline tags
        self.last_entity_id = entity_id
        
        # Get player/controller
        player_id = entity_data.get('player', 1)
        
        # Check if this is a Hero card
        if card_id and 'HERO' in card_id.upper():
            self.hero_entities[player_id] = entity_id
        
        # ALWAYS create entity, even without cardId (hidden deck cards)
        if card_id:
            # Known card - create real entity
            entity = self._get_or_create_entity(entity_id, entity_data)
            
            # Load card data from database and update entity attributes
            if entity:
                try:
                    if hasattr(entity, 'card_id') and not isinstance(getattr(type(entity), 'card_id', None), property):
                        entity.card_id = card_id
                    card_data = CardDatabase.get_card(card_id)
                    if card_data:
                        entity.data = card_data
                        entity.name = getattr(card_data, 'name', card_id)
                        entity.cost = getattr(card_data, 'cost', 0)
                        if hasattr(card_data, 'attack'):
                            entity.attack = card_data.attack
                        if hasattr(card_data, 'health'):
                            entity.health = card_data.health
                            entity.max_health = card_data.health
                except (AttributeError, TypeError):
                    pass  # Some entities (Hero, HeroPower) have read-only properties
        else:
            # Hidden card (in deck) - create placeholder that will be revealed later
            entity = self._create_placeholder_entity(entity_id, player_id)
        
        if entity:
            # Determine zone from the line if present
            zone_match = re.search(r'zone=(\w+)', line, re.IGNORECASE)
            if zone_match:
                zone_str = zone_match.group(1).upper()
                try:
                    new_zone = Zone[zone_str]
                    self._move_to_zone(entity, new_zone)
                    
                    # LOCAL PLAYER DETECTION: Cards going to HAND with known cardId = local player
                    if new_zone == Zone.HAND and card_id and self.local_player_id is None:
                        self.local_player_id = player_id
                        print(f"[Parser] Detected local player = Player {player_id} (visible card in hand)")
                    
                    return True
                except KeyError:
                    pass
        return False

    def _handle_show_entity(self, entity_id: int, card_id: str, line: str = ""):
        """Handle revealed cards (opponent's cards becoming known)."""
        entity = None
        
        if entity_id in self.entity_map:
            entity = self.entity_map[entity_id]
        else:
            # Entity doesn't exist yet - create a placeholder and add to map
            # Try to determine player from line (zone=HAND usually has player info)
            player_id = 1  # Default to player 1
            player_match = re.search(r'player=(\d+)', line)
            if player_match:
                player_id = int(player_match.group(1))
            
            # Create the entity
            entity = self._create_placeholder_entity(entity_id, player_id)
        
        if entity:
            # Update the card's identity
            if hasattr(entity, 'card_id'):
                entity.card_id = card_id
                # Load card data
                card_data = CardDatabase.get_card(card_id)
                if card_data:
                    entity.data = card_data
                    # Also update direct attributes that CardInstance reads
                    entity.name = getattr(card_data, 'name', card_id)
                    entity.cost = getattr(card_data, 'cost', 0)
                    if hasattr(card_data, 'attack'):
                        entity.attack = card_data.attack
                    if hasattr(card_data, 'health'):
                        entity.health = card_data.health
                        entity.max_health = card_data.health
                    print(f"[SHOW_ENTITY] id={entity_id} -> {entity.name} (cost {entity.cost})")
                else:
                    print(f"[SHOW_ENTITY] id={entity_id} cardId={card_id} NOT FOUND in database!")
            
            # Update zone if present in the SHOW_ENTITY line
            if line:
                zone_match = re.search(r'zone=(\w+)', line, re.IGNORECASE)
                if zone_match:
                    zone_str = zone_match.group(1).upper()
                    try:
                        new_zone = Zone[zone_str]
                        self._move_to_zone(entity, new_zone)
                    except KeyError:
                        pass
                    
    def _handle_attack(self, attacker_id: int, target_id: int):
        """Track attack events for visualization."""
        # This can be used to trigger arrow display
        pass  # The overlay handles this through the brain suggestions
        
    def _recalculate_mana(self, player):
        """Recalculate current mana based on crystals, usage and temp mana."""
        used = getattr(player, 'raw_resources_used', 0)
        # Mana = (Crystals - Used) + Temp
        # Note: Overload is handled by locked crystals usually, but for display this is main formula
        current = player.mana_crystals - used + player.temp_mana
        player.mana = max(0, current)

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
        
        elif tag == "ATK":
            if entity_id != -1:
                entity = self._get_or_create_entity(entity_id, entity_data)
                if entity and hasattr(entity, 'attack'):
                    try:
                        entity.attack = int(value)
                        state_changed = True
                    except ValueError:
                        pass
                        
        elif tag == "COST":
            if entity_id != -1:
                entity = self._get_or_create_entity(entity_id, entity_data)
                if entity: # Cost might be on card or placeholder
                    try:
                        # Some entities might rely on data.cost, but we try to set instance cost
                        entity.cost = int(value)
                        state_changed = True
                    except (ValueError, AttributeError):
                        pass

        elif tag == "DAMAGE":
            if entity_id != -1:
                entity = self._get_or_create_entity(entity_id, entity_data)
                if entity:
                    try:
                        entity.damage = int(value)
                        state_changed = True
                    except (ValueError, AttributeError):
                        pass
                        
        elif tag == "FROZEN":
            if entity_id != -1:
                entity = self._get_or_create_entity(entity_id, entity_data)
                if entity:
                    try:
                        entity.frozen = (value == "1")
                        state_changed = True
                    except (ValueError, AttributeError):
                        pass

        # === MANA UPDATES ===
        elif tag == "RESOURCES": # Max Mana
            if entity_id != -1:
                player = self._find_player_by_entity_id(entity_id)
                if player:
                    try:
                        player.mana_crystals = int(value)
                        self._recalculate_mana(player)
                        state_changed = True
                        
                        # Exit mulligan when first mana is received
                        if player.mana_crystals > 0 and self.in_mulligan:
                            self.in_mulligan = False
                            self.mulligan_complete = True
                    except ValueError:
                        pass
                        
        elif tag == "RESOURCES_USED": # Spent Mana
            if entity_id != -1:
                player = self._find_player_by_entity_id(entity_id)
                if player:
                    try:
                        player.raw_resources_used = int(value)
                        self._recalculate_mana(player)
                        state_changed = True
                    except ValueError:
                        pass
        
        elif tag == "TEMP_RESOURCES": # Coin/Innervate
             if entity_id != -1:
                player = self._find_player_by_entity_id(entity_id)
                if player:
                    try:
                         player.temp_mana = int(value) 
                         self._recalculate_mana(player)
                         state_changed = True
                    except:
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
                        
        # === ATTACK STATE ===
        elif tag == "EXHAUSTED":
             if entity_id != -1:
                entity = self._get_or_create_entity(entity_id, entity_data)
                if entity:
                     entity.exhausted = (value == "1")
                     state_changed = True
                     
        elif tag == "NUM_ATTACKS_THIS_TURN":
             if entity_id != -1:
                entity = self._get_or_create_entity(entity_id, entity_data)
                if entity:
                     try:
                        entity.num_attacks_this_turn = int(value)
                        state_changed = True
                     except ValueError:
                        pass
                
        # === CURRENT PLAYER ===
        elif tag == "CURRENT_PLAYER":
            if value == "1":
                # Entity becoming current player
                # In HS logs: Entity ID 2 = Player 1, Entity ID 3 = Player 2 typically
                # Or use 'player' field from entity_data
                player_num = entity_data.get('player')
                if player_num:
                    self.current_player_id = player_num
                    self.game.current_player_idx = player_num - 1
                    state_changed = True
                elif entity_id in [2, 3]:
                    # Fallback: entity ID 2 = player 1, ID 3 = player 2
                    self.current_player_id = entity_id - 1
                    self.game.current_player_idx = entity_id - 2
                    state_changed = True
                            
        # === STEP (Game Phase) ===
        elif tag == "STEP":
            # MAIN_READY = Mulligan complete, main game starts
            if value == "MAIN_READY" or value == "MAIN_ACTION":
                self.in_mulligan = False
                self.mulligan_complete = True
                state_changed = True
            # MAIN_START = Beginning of a turn
            elif value == "MAIN_START":
                state_changed = True
            # FINAL_GAMEOVER = Game ended
            elif value == "FINAL_GAMEOVER":
                self.in_game = False
                state_changed = True
                            
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
        """Parses entity string. Handles:
        - Plain ID: '42'
        - Full entity: '[entityName=... id=X ... cardId=Y player=Z]'
        - Nested brackets: '[entityName=UNKNOWN ENTITY [cardType=INVALID] id=X ...]'
        - Player names: 'HippieRogue#1926' (matched to player by name)
        """
        entity_str = entity_str.strip()
        result = {'id': -1}
        
        # Case 1: Plain numeric ID (e.g., "42")
        if entity_str.isdigit():
            result['id'] = int(entity_str)
            return result
        
        # Case 2: Player name (e.g., "HippieRogue#1926")
        # Try to resolve to known player OR bind strictly new name
        # This handles dynamic binding of names if we joined mid-game
        # Only try if string looks like a name (not containing brackets or signs effectively)
        # Simple heuristic: if it has no '=', it's likely a name (or a very weird string)
        if '=' not in entity_str and '[' not in entity_str:
            resolved_player = self._resolve_player_name(entity_str)
            if resolved_player:
                 # Find index
                 i = self.game.players.index(resolved_player)
                 # Map to Entity ID (P1=2, P2=3) 
                 # Note: This assumes P1 is always Entity 2. In some modes/logs this varies,
                 # but for 1v1 Standard it's safe enough.
                 result['id'] = i + 2
                 result['player'] = i + 1
                 return result
        
        # Case 3: Extract ID from anywhere in the string using regex
        # This handles nested brackets because we search the WHOLE string for id=X
        id_match = re.search(r'id=(\d+)', entity_str)
        if id_match:
            result['id'] = int(id_match.group(1))
        
        # Extract other fields from the string
        cardId_match = re.search(r'cardId=(\S+?)[\s\]]', entity_str)
        if cardId_match: 
            result['cardId'] = cardId_match.group(1)
        
        player_match = re.search(r'player=(\d+)', entity_str)
        if player_match: 
            result['player'] = int(player_match.group(1))
        
        zonePos_match = re.search(r'zonePos=(\d+)', entity_str)
        if zonePos_match: 
            result['zonePos'] = int(zonePos_match.group(1))
        
        return result

    def _handle_zone_change(self, entity_id: int, zone_value: str, entity_data: dict) -> bool:
        """Moves card between zones."""
        try:
            new_zone = Zone[zone_value]
        except KeyError:
            return False
        
        # Check if entity exists in map
        if entity_id in self.entity_map:
            entity = self.entity_map[entity_id]
            return self._move_to_zone(entity, new_zone)
        else:
            # Entity not in map - create a placeholder for zone tracking
            player_id = entity_data.get('player', 1)
            placeholder = self._create_placeholder_entity(entity_id, player_id)
            return self._move_to_zone(placeholder, new_zone)

    def _create_placeholder_entity(self, entity_id: int, player_id: int = 1):
        """Creates a placeholder entity for hidden/unknown cards."""
        # Already exists? Return it
        if entity_id in self.entity_map:
            return self.entity_map[entity_id]
        
        controller_idx = player_id - 1 if isinstance(player_id, int) else 0
        
        if 0 <= controller_idx < len(self.game.players):
            controller = self.game.players[controller_idx]
        else:
            controller = self.game.players[0]
        
        from simulator.enums import CardType
        
        class PlaceholderData:
            def __init__(self):
                self.cost = 0
                self.name = "Unknown"
                self.card_id = "UNKNOWN"
                self.text = ""
                self.attack = 0
                self.health = 1
        
        class PlaceholderCard:
            def __init__(self, ctrl, eid):
                self.controller = ctrl
                self.zone = Zone.DECK  # Assume it was in deck
                self.entity_id = eid
                self.card_id = "UNKNOWN"
                self.cost = 0
                self.data = PlaceholderData()
                self.card_type = CardType.MINION  # Default
                self.attack = 0
                self.health = 1
                self.max_health = 1
                self.damage = 0
                self.taunt = False
                self.divine_shield = False
                self.stealth = False
                self.windfury = False
                self.poisonous = False
                self.lifesteal = False
                self.rush = False
                self.charge = False
                self.frozen = False
                self.exhausted = True
                self.name = "Unknown Card"
                self.zone_position = 0
                
            def can_attack(self):
                return False
        
        placeholder = PlaceholderCard(controller, entity_id)
        self.entity_map[entity_id] = placeholder
        return placeholder

    def _move_to_zone(self, entity, new_zone: Zone) -> bool:
        """Move entity to a new zone."""
        if not hasattr(entity, 'zone'):
            return False
        if not hasattr(entity, 'controller'):
            return False
            
        old_zone = entity.zone
        if old_zone == new_zone:
            return False
            
        controller = entity.controller
        if not controller:
            return False
        
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
            
        # Try to create if cardId is present
        if data.get('cardId'):
            card_id = data['cardId']
            controller_idx = data.get('player', 1) - 1
            
            # Safe controller access
            if 0 <= controller_idx < len(self.game.players):
                controller = self.game.players[controller_idx]
            else:
                controller = self.game.players[0]
            
            from simulator.factory import create_card
            new_entity = create_card(card_id, controller)
            
            if new_entity:
                new_entity.entity_id = entity_id
                if 'zonePos' in data:
                    new_entity.zone_position = data['zonePos']
                
                self.entity_map[entity_id] = new_entity
                return new_entity

        return None

    def _find_player_by_entity_id(self, entity_id: int):
        """Finds player object by their Hero entity ID or Player entity ID.
        
        In Hearthstone logs:
        - Entity ID 1 = GameEntity
        - Entity ID 2 = Player 1's player entity  
        - Entity ID 3 = Player 2's player entity
        - Higher IDs = cards, heroes, etc.
        """
        # Direct player entity mapping (IDs 2 and 3 are player entities in HS)
        if entity_id == 2:
            return self.game.players[0] if len(self.game.players) > 0 else None
        if entity_id == 3:
            return self.game.players[1] if len(self.game.players) > 1 else None
        
        # Check hero entities
        for player_idx, hero_id in self.hero_entities.items():
            if hero_id == entity_id:
                if player_idx - 1 < len(self.game.players):
                    return self.game.players[player_idx - 1]
        
        # If we can't find by ID, try looking up the entity in map and checking controller
        if entity_id in self.entity_map:
            ent = self.entity_map[entity_id]
            if hasattr(ent, 'controller'):
                 # If entity is the PLAYER object itself
                 if ent.__class__.__name__ == 'Player':
                     return ent
                 # If entity is a HERO, return its controller
                 if ent.__class__.__name__ == 'Hero':
                     return ent.controller
        
        return None
    
    def is_local_player_turn(self) -> bool:
        """Check if it's the local player's turn."""
        if self.local_player_id is None or self.current_player_id is None:
            return False
        return self.local_player_id == self.current_player_id
    
    def get_local_player(self) -> Optional[Player]:
        """Get the local player object."""
        if self.local_player_id is not None:
            idx = self.local_player_id - 1
            if 0 <= idx < len(self.game.players):
                return self.game.players[idx]
        
        # Fallback: find player with named cards (your cards have visible cardIds)
        for p in self.game.players:
            for card in p.hand:
                if hasattr(card, 'data') and card.data and hasattr(card.data, 'name'):
                    if card.data.name != "Unknown":
                        return p
        
        # Default to player 0
        return self.game.players[0] if self.game.players else None
