"""Effect for Fire Plume's Heart (UNG_934).

Card Text: [x]<b>Quest:</b> Play
7 <b>Taunt</b> minions.
<b>Reward:</b> Sulfuras.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass