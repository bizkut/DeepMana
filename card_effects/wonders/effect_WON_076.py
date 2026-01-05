"""Effect for Anub'arak (WON_076).

Card Text: <b>Deathrattle:</b> Summon a 4/4 Nerubian with "<b>Deathrattle:</b> 
Summon Anub'arak."
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_076t")