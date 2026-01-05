"""Effect for Raid the Sky Temple (ULD_433).

Card Text: <b>Quest:</b> Cast 10 spells.
<b>Reward: </b>Ascendant Scroll.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass