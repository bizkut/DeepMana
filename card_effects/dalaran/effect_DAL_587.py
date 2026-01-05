"""Effect for Shimmerfly (DAL_587).

Card Text: <b>Deathrattle:</b> Add a random Hunter spell to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass