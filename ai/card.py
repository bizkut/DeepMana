"""Card representation module for HearthstoneOne AI."""

from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, List


class CardType(Enum):
    """Types of cards in Hearthstone."""
    MINION = auto()
    SPELL = auto()
    WEAPON = auto()
    HERO = auto()
    HERO_POWER = auto()


class CardRarity(Enum):
    """Card rarity levels."""
    FREE = auto()
    COMMON = auto()
    RARE = auto()
    EPIC = auto()
    LEGENDARY = auto()


class CardClass(Enum):
    """Hearthstone classes."""
    NEUTRAL = auto()
    DRUID = auto()
    HUNTER = auto()
    MAGE = auto()
    PALADIN = auto()
    PRIEST = auto()
    ROGUE = auto()
    SHAMAN = auto()
    WARLOCK = auto()
    WARRIOR = auto()
    DEMON_HUNTER = auto()
    DEATH_KNIGHT = auto()


@dataclass(frozen=True)
class CardInfo:
    """
    Immutable representation of a card's static attributes.
    
    Attributes:
        card_id: Unique identifier (e.g., "CS2_022" for Polymorph)
        name: Display name
        card_type: Type of card (MINION, SPELL, etc.)
        cost: Mana cost
        attack: Attack value (for minions/weapons)
        health: Health value (for minions)
        durability: Durability (for weapons)
        card_class: Class restriction
        rarity: Card rarity
        text: Card text/description
        keywords: Special keywords (Taunt, Divine Shield, etc.)
    """
    card_id: str
    name: str
    card_type: CardType
    cost: int
    attack: Optional[int] = None
    health: Optional[int] = None
    durability: Optional[int] = None
    card_class: CardClass = CardClass.NEUTRAL
    rarity: CardRarity = CardRarity.FREE
    text: str = ""
    keywords: tuple = ()
    
    def is_minion(self) -> bool:
        """Check if this card is a minion."""
        return self.card_type == CardType.MINION
    
    def is_spell(self) -> bool:
        """Check if this card is a spell."""
        return self.card_type == CardType.SPELL
    
    def is_weapon(self) -> bool:
        """Check if this card is a weapon."""
        return self.card_type == CardType.WEAPON


@dataclass
class CardInstance:
    """
    A card instance in the game (in hand, on board, etc.).
    
    Unlike CardInfo, this represents the current state of a card
    which can change during the game (e.g., buffed stats).
    
    Attributes:
        info: Static card information
        current_cost: Current mana cost (can be modified)
        current_attack: Current attack (for minions on board)
        current_health: Current health (for minions on board)
        can_attack: Whether minion can attack this turn
        is_exhausted: Whether minion just entered play
        zone_position: Position in the zone (hand index, board position)
    """
    info: CardInfo
    current_cost: int
    current_attack: Optional[int] = None
    current_health: Optional[int] = None
    max_health: Optional[int] = None
    can_attack: bool = False
    is_exhausted: bool = True
    has_taunt: bool = False
    has_divine_shield: bool = False
    has_stealth: bool = False
    is_frozen: bool = False
    zone_position: int = 0
    
    @classmethod
    def from_simulator_card(cls, sim_card) -> "CardInstance":
        """Create a CardInstance from a Simulator card object."""
        from simulator.enums import CardType as SimCardType
        
        # Map Type
        if sim_card.card_type == SimCardType.MINION:
            card_type = CardType.MINION
        elif sim_card.card_type == SimCardType.SPELL:
            card_type = CardType.SPELL
        elif sim_card.card_type == SimCardType.WEAPON:
            card_type = CardType.WEAPON
        elif sim_card.card_type == SimCardType.HERO_POWER:
            card_type = CardType.HERO_POWER
        elif sim_card.card_type == SimCardType.HERO:
            card_type = CardType.HERO
        else:
            card_type = CardType.MINION
        
        # Get card data with fallbacks for missing data
        data = getattr(sim_card, 'data', None)
        
        # Name: prefer sim_card.name (set by parser), fallback to data.name
        name = getattr(sim_card, 'name', None) or (data.name if data and hasattr(data, 'name') else "Unknown Card")
        
        # Cost: prefer data.cost, fallback to sim_card.cost
        base_cost = (data.cost if data and hasattr(data, 'cost') else None) or getattr(sim_card, 'cost', 0)
        
        # Attack/Health: prefer data, fallback to sim_card attributes
        base_attack = (data.attack if data and hasattr(data, 'attack') else None) or getattr(sim_card, 'attack', None)
        base_health = (data.health if data and hasattr(data, 'health') else None) or getattr(sim_card, 'health', None)
        
        info = CardInfo(
            card_id=getattr(sim_card, 'card_id', ''),
            name=name,
            card_type=card_type,
            cost=base_cost,
            attack=base_attack,
            health=base_health,
            text=data.text if data and hasattr(data, 'text') else "",
        )
        
        return cls(
            info=info,
            current_cost=getattr(sim_card, 'cost', base_cost),
            current_attack=getattr(sim_card, 'attack', base_attack),
            current_health=getattr(sim_card, 'health', base_health),
            max_health=getattr(sim_card, 'max_health', base_health),
            can_attack=sim_card.can_attack() if hasattr(sim_card, 'can_attack') else False,
            is_exhausted=getattr(sim_card, 'exhausted', True),
            has_taunt=getattr(sim_card, 'taunt', False),
            has_divine_shield=getattr(sim_card, 'divine_shield', False),
            has_stealth=getattr(sim_card, 'stealth', False),
            is_frozen=getattr(sim_card, 'frozen', False),
            zone_position=getattr(sim_card, 'zone_position', 0)
        )

    @classmethod
    def from_fireplace_card(cls, fp_card) -> "CardInstance":
        """
        Create a CardInstance from a Fireplace card object.
        
        Args:
            fp_card: Fireplace card entity
            
        Returns:
            CardInstance representing the card's current state
        """
        # Determine card type using hearthstone.enums.CardType
        from hearthstone.enums import CardType as HSCardType
        
        fp_type = getattr(fp_card, 'type', None)
        if fp_type == HSCardType.MINION:
            card_type = CardType.MINION
        elif fp_type == HSCardType.SPELL:
            card_type = CardType.SPELL
        elif fp_type == HSCardType.WEAPON:
            card_type = CardType.WEAPON
        elif fp_type == HSCardType.HERO_POWER:
            card_type = CardType.HERO_POWER
        elif fp_type == HSCardType.HERO:
            card_type = CardType.HERO
        else:
            card_type = CardType.MINION  # Default fallback
        
        # Build CardInfo
        info = CardInfo(
            card_id=fp_card.id,
            name=getattr(fp_card, 'name', fp_card.id),
            card_type=card_type,
            cost=getattr(fp_card, 'cost', 0),
            attack=getattr(fp_card, 'atk', None),
            health=getattr(fp_card, 'health', None),
        )
        
        # Build instance with current state
        instance = cls(
            info=info,
            current_cost=getattr(fp_card, 'cost', 0),
            current_attack=getattr(fp_card, 'atk', None),
            current_health=getattr(fp_card, 'health', None),
            max_health=getattr(fp_card, 'max_health', None),
            can_attack=getattr(fp_card, 'can_attack', lambda: False)() if callable(getattr(fp_card, 'can_attack', None)) else getattr(fp_card, 'can_attack', False),
            is_exhausted=getattr(fp_card, 'exhausted', True),
            has_taunt=getattr(fp_card, 'taunt', False),
            has_divine_shield=getattr(fp_card, 'divine_shield', False),
            has_stealth=getattr(fp_card, 'stealthed', False),
            is_frozen=getattr(fp_card, 'frozen', False),
        )
        
        return instance
    
    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "card_id": self.info.card_id,
            "name": self.info.name,
            "type": self.info.card_type.name,
            "base_cost": self.info.cost,
            "current_cost": self.current_cost,
            "attack": self.current_attack,
            "health": self.current_health,
            "max_health": self.max_health,
            "can_attack": self.can_attack,
            "taunt": self.has_taunt,
            "divine_shield": self.has_divine_shield,
            "stealth": self.has_stealth,
            "frozen": self.is_frozen,
            "position": self.zone_position,
        }
