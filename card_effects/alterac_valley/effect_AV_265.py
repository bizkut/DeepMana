"""Effect for Ur'zul Giant (AV_265).

Card Text: Costs (1) less for each friendly minion that died this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass