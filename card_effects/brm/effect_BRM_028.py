"""Effect for Emperor Thaurissan (BRM_028).

Card Text: At the end of your turn, reduce the Cost of cards
in your hand by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass