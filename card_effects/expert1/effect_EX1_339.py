"""Effect for Thoughtsteal (EX1_339).

Card Text: Copy 2 cards in your opponent's deck and add them to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass