"""Effect for Ferocious Felbat (EDR_892).

Card Text: [x]<b>Deathrattle:</b> Resurrect a
different friendly <b>Deathrattle</b>
minion that costs (5) or more.
Summon a copy of it.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EDR_892t")