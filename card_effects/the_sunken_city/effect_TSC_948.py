"""Effect for Gifts of Azshara (TSC_948).

Card Text: Draw a card. If you played a Naga while holding this, do it again.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)