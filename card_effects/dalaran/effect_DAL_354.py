"""Effect for Acornbearer (DAL_354).

Card Text: <b>Deathrattle:</b> Add two 1/1 Squirrels to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass