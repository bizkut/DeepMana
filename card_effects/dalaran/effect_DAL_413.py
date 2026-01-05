"""Effect for EVIL Conscripter (DAL_413).

Card Text: <b>Deathrattle:</b> Add a <b>Lackey</b> to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass