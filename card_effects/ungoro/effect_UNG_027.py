"""Effect for Pyros (UNG_027).

Card Text: <b>Deathrattle:</b> Return this to your hand as a 6/6 that costs (4).
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass