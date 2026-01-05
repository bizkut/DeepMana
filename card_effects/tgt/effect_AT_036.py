"""Effect for Anub'arak (AT_036).

Card Text: <b>Deathrattle:</b> Summon a 4/4 Nerubian with "<b>Deathrattle:</b> 
Summon Anub'arak."
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AT_036t")