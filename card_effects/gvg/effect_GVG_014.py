"""Effect for Vol'jin (GVG_014).

Card Text: <b>Battlecry:</b> Swap Health with another minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)