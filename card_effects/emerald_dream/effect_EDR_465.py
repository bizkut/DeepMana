"""Effect for Ysondre (EDR_465).

Card Text: [x]<b>Taunt</b>. <b>Deathrattle:</b> Summon
a random Dragon for each
time Ysondre has died
this game.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EDR_465t")