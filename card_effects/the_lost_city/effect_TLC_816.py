"""Effect for Gravedawn Sunbloom (TLC_816).

Card Text: Draw 2 cards. <b>Kindred:</b> This costs (2) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)