"""Effect for Wing Commander Ichman (AV_336).

Card Text: [x]<b>Battlecry:</b> Summon a Beast
from your deck and give it
<b>Rush</b>. If it kills a minion
this turn, repeat.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_336t")