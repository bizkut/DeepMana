"""Effect for Mukla's Champion (AT_090).

Card Text: <b>Inspire:</b> Give your other minions +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1