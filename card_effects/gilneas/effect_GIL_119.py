"""Effect for Cauldron Elemental (GIL_119).

Card Text: Your other Elementals have +2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2