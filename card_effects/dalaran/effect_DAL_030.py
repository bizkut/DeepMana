"""Effect for Shadowy Figure (DAL_030).

Card Text: <b>Battlecry:</b> Transform into a 2/2 copy of a friendly <b>Deathrattle</b> minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass