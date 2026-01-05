"""Effect for Dread Raven (DRG_088).

Card Text: Has +3 Attack for each other Dread Raven you control.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3