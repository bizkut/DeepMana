"""Effect for Call Pet (GVG_017).

Card Text: Draw a card.
If it's a Beast, it costs (4) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(4)