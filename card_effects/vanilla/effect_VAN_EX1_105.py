"""Effect for Mountain Giant (VAN_EX1_105).

Card Text: Costs (1) less for each other card in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass