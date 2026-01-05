"""Effect for Mok'Nathal Lion (BT_212).

Card Text: <b>Rush</b>. <b>Battlecry:</b> Choose a friendly minion. Gain a copy of its <b>Deathrattle</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass