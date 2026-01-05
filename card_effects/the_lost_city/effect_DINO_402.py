"""Effect for Bat Mask (DINO_402).

Card Text: Set a friendly minion's stats to 1/1. Fill your board with copies of it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass