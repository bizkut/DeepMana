"""Effect for Forged in Flame (TSC_939).

Card Text: Destroy your weapon, then draw cards equal to its Attack.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)