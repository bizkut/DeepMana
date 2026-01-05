"""Effect for Aldor Attendant (BT_020).

Card Text: <b>Battlecry:</b> Reduce the Cost of your Librams by (1) this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass