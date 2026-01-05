"""Effect for Reluctant Wrangler (TLC_443).

Card Text: [x]<b>Reborn</b>
<b>Deathrattle:</b> Summon a 2/2
Undead Beast with <b>Taunt</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_443t")