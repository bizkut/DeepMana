"""Effect for Volcanic Drake (BRM_025).

Card Text: Costs (1) less for each minion that died this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass