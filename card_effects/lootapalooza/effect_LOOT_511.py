"""Effect for Kathrena Winterwisp (LOOT_511).

Card Text: <b>Battlecry and Deathrattle:</b> <b>Recruit</b> a Beast.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass