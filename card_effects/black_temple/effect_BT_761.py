"""Effect for Coilfang Warlord (BT_761).

Card Text: [x]<b>Rush</b>
<b>Deathrattle:</b> Summon a
 5/9 Warlord with <b>Taunt</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_761t")