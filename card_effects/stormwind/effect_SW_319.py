"""Effect for Peasant (SW_319).

Card Text: At the start of your turn, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)