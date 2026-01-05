"""Effect for Righteous Defense (DED_502).

Card Text: Set a minion's Attack and Health to 1. Give the stats it lost to a minion in your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)