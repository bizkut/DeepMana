"""Effect for Vile Library (REV_371).

Card Text: Give a friendly minion +1/+1. Repeat for each Imp you control.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1