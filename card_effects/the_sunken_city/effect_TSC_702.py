"""Effect for Switcheroo (TSC_702).

Card Text: Draw 2 minions.
Swap their Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)