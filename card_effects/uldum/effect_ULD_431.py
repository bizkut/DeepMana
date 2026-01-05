"""Effect for Making Mummies (ULD_431).

Card Text: [x]<b>Quest:</b> Play 5 <b>Reborn</b>
minions.
<b>Reward:</b> Emperor Wraps.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass