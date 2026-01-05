"""Effect for Majordomo Executus (BRM_027).

Card Text: <b>Deathrattle:</b> Replace your hero with Ragnaros the Firelord.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass