"""Effect for Rat Pack (CFM_316).

Card Text: [x]<b>Deathrattle:</b> Summon a
number of 1/1 Rats equal
 to this minion's Attack.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CFM_316t")