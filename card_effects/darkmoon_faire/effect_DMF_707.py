"""Effect for Magicfin (DMF_707).

Card Text: After a friendly Murloc dies, add a random <b>Legendary</b> minion to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass