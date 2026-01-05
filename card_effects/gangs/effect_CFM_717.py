"""Effect for Jade Claws (CFM_717).

Card Text: <b>Battlecry:</b> Summon a{1} {0} <b>Jade Golem</b>.
<b><b>Overload</b>:</b> (1)0<b>Battlecry:</b> Summon a <b>Jade Golem</b>.
<b><b>Overload</b>:</b> (1)
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CFM_717t")