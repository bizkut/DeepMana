"""Effect for Vile Apothecary (RLK_571).

Card Text: At the end of your turn,
add a random Concoction to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass