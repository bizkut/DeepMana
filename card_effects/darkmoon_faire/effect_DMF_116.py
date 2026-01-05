"""Effect for The Nameless One (DMF_116).

Card Text: <b>Battlecry:</b> Choose a minion. Become a 4/4 copy of it, then <b>Silence</b> it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.silence(target)