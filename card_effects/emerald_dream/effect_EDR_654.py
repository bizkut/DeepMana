"""Effect for Overgrown Horror (EDR_654).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> Reduce the Cost
of minions in your hand
with <b>Dark Gifts</b> by (2).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass