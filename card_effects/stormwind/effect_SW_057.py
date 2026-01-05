"""Effect for Package Runner (SW_057).

Card Text: Can only attack if you have at least 8 cards in hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass