"""Effect for Light's Champion (AT_106).

Card Text: <b>Battlecry:</b> <b>Silence</b> a Demon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.silence(target)