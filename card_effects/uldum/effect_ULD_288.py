"""Effect for Anka, the Buried (ULD_288).

Card Text: <b>Battlecry:</b> Change each <b>Deathrattle</b> minion in your hand into a 1/1 that costs (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass