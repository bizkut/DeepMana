"""Effect for Open the Waygate (UNG_028).

Card Text: [x]<b>Quest:</b> Cast 8 spells that
didn't start in your deck.
<b>Reward:</b> Time Warp.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass