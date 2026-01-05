"""Effect for Ysera (VAN_EX1_572).

Card Text: At the end of your turn, add a Dream Card to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass