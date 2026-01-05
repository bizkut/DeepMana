"""Effect for Tomb Pillager (CORE_LOE_012).

Card Text: <b>Deathrattle:</b> Get a Coin.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass