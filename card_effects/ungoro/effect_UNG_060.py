"""Effect for Mimic Pod (UNG_060).

Card Text: Draw a card, then add a copy of it to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)