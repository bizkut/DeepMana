"""Effect for Chromaggus (BRM_031).

Card Text: Whenever you draw a card, put another copy into your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)