"""Effect for Oblivitron (DAL_376).

Card Text: [x]<b>Deathrattle:</b> Summon a
Mech from your hand and
trigger its <b>Deathrattle</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_376t")