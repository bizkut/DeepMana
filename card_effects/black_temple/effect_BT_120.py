"""Effect for Warmaul Challenger (BT_120).

Card Text: <b>Battlecry:</b> Choose
an enemy minion.
Battle it to the death!
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass