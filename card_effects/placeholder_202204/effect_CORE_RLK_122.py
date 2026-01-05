"""Effect for The Scourge (CORE_RLK_122).

Card Text: Fill your board with random Undead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass