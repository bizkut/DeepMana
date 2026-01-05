"""Effect for Fireguard Destroyer (BRM_012).

Card Text: <b>Battlecry:</b> Gain 1-4 Attack. <b>Overload:</b> (1)
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass