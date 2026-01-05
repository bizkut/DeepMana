"""Effect for Faceless Manipulator (VAN_EX1_564).

Card Text: <b>Battlecry:</b> Choose a minion and become a copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass