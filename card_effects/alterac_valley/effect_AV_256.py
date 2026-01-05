"""Effect for Reflecto Engineer (AV_256).

Card Text: <b>Battlecry:</b> Swap the Attack and Health of all minions in both players' hands.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)