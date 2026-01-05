"""Effect for Surging Tempest (DRG_216).

Card Text: Has +1 Attack while you have <b>Overloaded</b> Mana Crystals.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1