"""Effect for Abyssal Depths (TSC_608).

Card Text: Draw your two lowest Cost minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)