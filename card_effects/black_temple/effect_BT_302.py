"""Effect for The Dark Portal (BT_302).

Card Text: Draw a minion. If you have at least 8 cards in hand, it costs (5) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(8)