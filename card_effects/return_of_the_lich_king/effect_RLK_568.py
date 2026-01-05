"""Effect for Concoctor (RLK_568).

Card Text: <b>Battlecry:</b> Add a random Concoction to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass