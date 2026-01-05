"""Effect for Raid Boss Onyxia (ONY_004).

Card Text: [x]<b>Rush</b>. <b>Immune</b> while
you control a Whelp.
<b>Battlecry:</b> Summon six
 2/1 Whelps with <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ONY_004t")