"""Effect for Ini Stormcoil (TSC_649).

Card Text: [x]<b>Battlecry:</b> Choose a friendly
Mech. Summon a copy of it
with <b>Rush</b>, <b>Windfury</b>, and
<b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TSC_649t")