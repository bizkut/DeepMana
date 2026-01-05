"""Effect for Saronite Chain Gang (CORE_ICC_466).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> Summon a
copy of this minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_ICC_466t")