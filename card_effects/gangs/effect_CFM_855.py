"""Effect for Defias Cleaner (CFM_855).

Card Text: <b>Battlecry:</b> <b>Silence</b> a minion with <b>Deathrattle</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.silence(target)


def deathrattle(game, source):
    pass