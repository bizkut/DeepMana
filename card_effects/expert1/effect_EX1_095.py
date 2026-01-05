"""Effect for Gadgetzan Auctioneer (EX1_095).

Card Text: Whenever you cast a spell, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)