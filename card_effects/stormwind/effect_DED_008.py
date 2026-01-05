"""Effect for Monstrous Parrot (DED_008).

Card Text: <b>Battlecry</b>: Get a copy of the last friendly <b>Deathrattle</b> minion that died.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass