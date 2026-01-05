"""Effect for Evolve (OG_027).

Card Text: Transform your minions into random minions that cost (1) more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass