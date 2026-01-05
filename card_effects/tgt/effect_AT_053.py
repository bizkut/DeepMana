"""Effect for Ancestral Knowledge (AT_053).

Card Text: Draw 2 cards. <b>Overload:</b> (1)
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)