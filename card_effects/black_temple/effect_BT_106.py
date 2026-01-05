"""Effect for Bogstrok Clacker (BT_106).

Card Text: <b>Battlecry:</b> Transform adjacent minions into random minions that cost (1) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass