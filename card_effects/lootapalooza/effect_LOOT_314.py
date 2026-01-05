"""Effect for Grizzled Guardian (LOOT_314).

Card Text: <b>Taunt</b>
<b>Deathrattle:</b> <b>Recruit</b> 2 minions that cost (4) or less.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass