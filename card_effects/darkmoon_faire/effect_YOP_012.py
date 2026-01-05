"""Effect for Deathwarden (YOP_012).

Card Text: <b>Deathrattles</b> can't trigger.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass