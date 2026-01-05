"""Effect for Moat Lurker (KAR_041).

Card Text: <b>Battlecry:</b> Destroy a minion. <b>Deathrattle:</b> Resummon it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "KAR_041t")


def deathrattle(game, source):
    pass