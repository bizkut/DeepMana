"""Effect for Fast Forward (TIME_770).

Card Text: Draw 2 cards.
Pick one to have its Cost reduced by (2).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)