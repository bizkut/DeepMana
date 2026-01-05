"""Effect for Necromechanic (BOT_039).

Card Text: Your <b>Deathrattles</b> trigger twice.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass