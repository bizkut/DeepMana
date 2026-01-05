"""Effect for Far Sight (CS2_053).

Card Text: Draw a card. That card costs (3) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)