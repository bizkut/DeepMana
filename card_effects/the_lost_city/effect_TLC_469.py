"""Effect for Tunnel Terror (TLC_469).

Card Text: <b>Deathrattle:</b> Get two random <b>Temporary</b>
2-Cost minions.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass