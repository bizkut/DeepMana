"""Effect for Doomhammer (VAN_EX1_567).

Card Text: <b>Windfury, Overload:</b> (2)
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass