"""Effect for Transmogrifier (DRG_092).

Card Text: Whenever you draw a card, transform it into a random <b>Legendary</b> minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)