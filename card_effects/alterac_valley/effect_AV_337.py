"""Effect for Mountain Bear (AV_337).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Summon two
2/4 Cubs with <b>Taunt</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_337t")