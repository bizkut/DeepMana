"""Effect for The Storm Bringer (BOT_245).

Card Text: Transform your minions into random <b>Legendary</b> minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass