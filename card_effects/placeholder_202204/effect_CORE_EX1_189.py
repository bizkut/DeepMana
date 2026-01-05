"""Effect for Brightwing (CORE_EX1_189).

Card Text: <b>Battlecry:</b> Add a random <b>Legendary</b> minion to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass