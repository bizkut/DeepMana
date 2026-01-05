"""Effect for Enhanced Dreadlord (BT_304).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Summon a 5/5
Dreadlord with <b>Lifesteal</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_304t")