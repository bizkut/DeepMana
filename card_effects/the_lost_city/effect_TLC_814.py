"""Effect for Twilight Mender (TLC_814).

Card Text: <b>Deathrattle:</b> Get a random Holy and Shadow spell.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass