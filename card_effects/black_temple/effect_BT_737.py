"""Effect for Maiev Shadowsong (BT_737).

Card Text: <b>Battlecry:</b> Choose a minion.
It goes <b>Dormant</b> for 2 turns.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass