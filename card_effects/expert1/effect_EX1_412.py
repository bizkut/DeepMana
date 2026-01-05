"""Effect for Raging Worgen (EX1_412).

Card Text: Has +1 Attack and <b>Windfury</b> while damaged.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1