"""Effect for Invocation of Frost (DRG_248).

Card Text: <b>Freeze</b> an enemy. 
<b>Invoke</b> Galakrond.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.frozen = True