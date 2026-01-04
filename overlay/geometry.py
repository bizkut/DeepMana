from dataclasses import dataclass
from typing import Tuple

@dataclass
class Point:
    x: int
    y: int

class HearthstoneGeometry:
    """
    Calculates screen coordinates for Hearthstone entities based on relative geometry.
    Assumes standard aspect ratio logic.
    """
    
    def __init__(self, width: int = 1920, height: int = 1080):
        self.width = width
        self.height = height
        
        # Geometry Constants (Relative 0.0-1.0)
        # Calibrated for 16:9 aspect ratio (1920x1080 / 2560x1440)
        self.HAND_Y_PCT = 0.92          # Cards in hand (raised from 0.95)
        self.PLAYER_BOARD_Y_PCT = 0.54  # Player's minions (slightly lower)
        self.OPPONENT_BOARD_Y_PCT = 0.43 # Opponent's minions
        self.OPPONENT_HERO_Y_PCT = 0.18  # Opponent hero portrait (approx)
        self.PLAYER_HERO_Y_PCT = 0.78    # Player hero portrait
        
        self.BOARD_CENTER_X_PCT = 0.5
        
    def resize(self, width: int, height: int):
        self.width = width
        self.height = height

    def _to_pixels(self, x_pct: float, y_pct: float) -> Point:
        return Point(int(x_pct * self.width), int(y_pct * self.height))

    def get_hand_card_pos(self, index: int, total_cards: int) -> Point:
        """Returns center position of a card in player's hand."""
        if total_cards <= 0: return self._to_pixels(0.5, 0.9)
        
        # Hand spread logic
        # Full hand (10 cards) covers about 65-70% of screen width
        # Cards arc slightly, but linear approx is okay for now
        
        max_spread = 0.65
        spread_per_card = 0.065
        
        current_spread = min(max_spread, total_cards * spread_per_card)
        
        if total_cards == 1:
            return self._to_pixels(0.5, self.HAND_Y_PCT)
            
        start_x = 0.5 - (current_spread / 2) + (current_spread / (total_cards * 2)) 
        step = current_spread / total_cards
        
        x_pct = start_x + (index * step)
        
        # Arc compensation (outer cards are lower)
        # Simple quadratic curve offset
        # dist_from_center = abs(index - (total_cards - 1) / 2)
        # y_offset = (dist_from_center ** 2) * 0.005
        
        return self._to_pixels(x_pct, self.HAND_Y_PCT)

    def get_player_minion_pos(self, index: int, total_minions: int) -> Point:
        """Returns center position of a minion on player's board."""
        return self._get_board_pos(index, total_minions, self.PLAYER_BOARD_Y_PCT)

    def get_opponent_minion_pos(self, index: int, total_minions: int) -> Point:
        """Returns center position of a minion on opponent's board."""
        return self._get_board_pos(index, total_minions, self.OPPONENT_BOARD_Y_PCT)

    def _get_board_pos(self, index: int, total_minions: int, y_pct: float) -> Point:
        if total_minions <= 0: return self._to_pixels(0.5, y_pct)
        
        # Board slots are fairly fixed width
        # 7 minions take up about 60% of width
        total_width_for_7 = 0.60
        slot_width = total_width_for_7 / 7
        
        current_spread = total_minions * slot_width
        
        # Start from center-left
        start_x = 0.5 - (current_spread / 2) + (slot_width / 2)
        
        x_pct = start_x + (index * slot_width)
        return self._to_pixels(x_pct, y_pct)

    def get_hero_pos(self, is_opponent: bool) -> Point:
        y = self.OPPONENT_HERO_Y_PCT if is_opponent else self.PLAYER_HERO_Y_PCT
        return self._to_pixels(0.5, y)
    
    def get_hero_power_pos(self, is_opponent: bool = False) -> Point:
        """Returns position of hero power button (right of hero portrait)."""
        y = self.OPPONENT_HERO_Y_PCT if is_opponent else self.PLAYER_HERO_Y_PCT
        # Adjusted X offset for hero power
        return self._to_pixels(0.59, y)
    
    def get_turn_button_pos(self) -> Point:
        return self._to_pixels(0.82, 0.45)  # Right side, middle
    
    def get_location_pos(self, index: int, total_locations: int, total_minions: int) -> Point:
        """Returns position of a location on the board."""
        total_board = total_minions + total_locations
        effective_index = total_minions + index
        return self._get_board_pos(effective_index, total_board, self.PLAYER_BOARD_Y_PCT)
