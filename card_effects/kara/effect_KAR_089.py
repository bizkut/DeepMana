"""Effect for Malchezaar's Imp (KAR_089).

Card Text: Whenever you discard a card, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)