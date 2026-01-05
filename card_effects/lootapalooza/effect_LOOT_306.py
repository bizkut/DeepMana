"""Effect for Possessed Lackey (LOOT_306).

Card Text: <b>Deathrattle:</b> <b>Recruit</b> a Demon.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass