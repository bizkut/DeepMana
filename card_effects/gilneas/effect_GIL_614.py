"""Effect for Voodoo Doll (GIL_614).

Card Text: <b>Battlecry:</b> Choose a minion. <b>Deathrattle:</b> Destroy the chosen minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()


def deathrattle(game, source):
    pass