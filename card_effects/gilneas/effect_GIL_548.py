"""Effect for Book of Specters (GIL_548).

Card Text: Draw 3 cards. Discard any spells drawn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)