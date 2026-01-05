"""Effect for Serena Bloodfeather (BAR_315).

Card Text: <b>Battlecry:</b> Choose an enemy minion. Steal Attack and Health from it until this has more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)