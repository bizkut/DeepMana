"""Effect for Infiltrator Lilian (SCH_426).

Card Text: [x]<b>Stealth</b>
<b>Deathrattle:</b> Summon a 4/2
Forsaken Lilian that attacks
a random enemy.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_426t")