"""Effect for The Marsh Queen (UNG_920).

Card Text: [x]<b>Quest:</b> Play seven
1-Cost minions.
<b>Reward:</b> Queen Carnassa.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass