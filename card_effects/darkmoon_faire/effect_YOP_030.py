"""Effect for Felfire Deadeye (YOP_030).

Card Text: Your Hero Power costs (1) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass