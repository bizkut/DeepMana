"""Effect for Hybridization (TLC_236).

Card Text: Draw a 1, 2, 3, and 4-Cost minion. <b>Kindred:</b> They cost (1) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)