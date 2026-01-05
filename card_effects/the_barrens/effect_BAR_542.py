"""Effect for Refreshing Spring Water (BAR_542).

Card Text: Draw 2 cards.
Refresh 2 Mana Crystals for each spell drawn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)