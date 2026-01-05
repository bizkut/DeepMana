"""Effect for Deadly Fork (KAR_094).

Card Text: <b>Deathrattle:</b> Add a 3/2 weapon to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass