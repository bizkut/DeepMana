"""Effect for Stoneborn General (CORE_REV_375).

Card Text: [x]<b>Rush</b> 
  <b>Deathrattle:</b> Summon an 
   8/8 Gravewing with <b>Rush</b>. 
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_REV_375t")