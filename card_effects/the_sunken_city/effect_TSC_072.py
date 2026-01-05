"""Effect for Conch's Call (TSC_072).

Card Text: Draw a Naga and
a spell.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)