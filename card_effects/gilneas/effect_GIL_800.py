"""Effect for Duskfallen Aviana (GIL_800).

Card Text: On each player's turn, the first card played costs (0).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass