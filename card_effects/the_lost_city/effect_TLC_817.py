"""Effect for Reach Equilibrium (TLC_817).

Card Text: [x]<b>Quest:</b> Cast 4 Holy spells
<b>Reward:</b> Life's Breath.
<b>Quest:</b> Cast 4 Shadow spells.
<b>Reward:</b> Death's Touch.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass