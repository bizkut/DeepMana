"""Effect for Celestial Ink Set (SW_001).

Card Text: [x]After you spend 5 Mana on
spells, reduce the Cost of a
spell in your hand by (5).
Lose 1 Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass