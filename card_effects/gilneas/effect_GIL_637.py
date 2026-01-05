"""Effect for Ferocious Howl (GIL_637).

Card Text: Draw a card.
Gain 1 Armor for each card in your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)