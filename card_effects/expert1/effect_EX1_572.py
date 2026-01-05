"""Effect for Ysera (EX1_572).

Card Text: At the end of your turn, get two random Dream cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass