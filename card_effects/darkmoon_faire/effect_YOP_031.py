"""Effect for Crabrider (YOP_031).

Card Text: <b><b>Rush</b>
Windfury</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass