"""Effect for The Scourge (RLK_122).

Card Text: Fill your board with random Undead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass