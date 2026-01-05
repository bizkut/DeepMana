"""Effect for Reanimate the Terror (TLC_433).

Card Text: [x]<b>Quest:</b> Spend 15 <b>Corpses</b>.
<b>Reward:</b> Tyrax, Bone Terror.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass