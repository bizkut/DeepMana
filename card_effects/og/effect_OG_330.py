"""Effect for Undercity Huckster (OG_330).

Card Text: <b>Deathrattle:</b> Get a
random card <i>(from your
opponent's class)</i>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass