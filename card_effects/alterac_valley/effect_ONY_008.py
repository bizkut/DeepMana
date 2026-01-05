"""Effect for Furious Howl (ONY_008).

Card Text: Draw a card.
Repeat until you have at least 3 cards.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)