"""Effect for Pterrordax Egg (TLC_831).

Card Text: [x]<b>Deathrattle:</b> Summon
a 3/3 Pterrordax that
steals 1 Health from
all other minions.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_831t")