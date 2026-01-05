"""Effect for Dust Devil (VAN_EX1_243).

Card Text: <b>Windfury</b>. <b>Overload:</b> (2)
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass