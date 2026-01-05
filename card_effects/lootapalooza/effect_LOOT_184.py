"""Effect for Silver Vanguard (LOOT_184).

Card Text: <b>Deathrattle:</b> <b>Recruit</b> an
8-Cost minion.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass