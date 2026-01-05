"""Effect for Devour Mind (CORE_ICC_207).

Card Text: Copy 3 cards in your opponent's deck and add them to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass