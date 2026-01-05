"""Effect for Renowned Performer (DMF_223).

Card Text: [x]<b>Rush</b>
<b>Deathrattle:</b> Summon two
  1/1 Assistants with <b>Taunt</b>.  
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_223t")