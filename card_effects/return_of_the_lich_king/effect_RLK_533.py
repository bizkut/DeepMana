"""Effect for Scourge Supplies (RLK_533).

Card Text: Draw 3 cards.
Choose one to discard.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)