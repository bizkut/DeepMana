"""Effect for Candle Breath (DRG_033).

Card Text: Draw 3 cards. Costs (3) less while you're holding a Dragon.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)