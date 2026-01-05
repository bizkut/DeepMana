"""Effect for Stormcoil Mothership (TSC_645).

Card Text: <b>Rush</b>
<b>Deathrattle:</b> Summon two random Mechs that cost (3) or less.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TSC_645t")