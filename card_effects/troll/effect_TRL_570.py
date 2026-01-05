"""Effect for Soup Vendor (TRL_570).

Card Text: Whenever you restore 3 or more Health to your hero, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)