"""Effect for Bronze Herald (DAL_146).

Card Text: <b>Deathrattle:</b> Add two 4/4 Dragons to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass