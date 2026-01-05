"""Effect for Webspinner (FP1_011).

Card Text: <b>Deathrattle:</b> Get a
random Beast.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass