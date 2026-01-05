"""Effect for Windfury Harpy (VAN_EX1_033).

Card Text: <b>Windfury</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass