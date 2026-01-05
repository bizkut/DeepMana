"""Effect for Cup o' Muscle (VAC_338t).

Card Text: [x]Give a minion in   your hand +2/+1.  <i>(2 Drinks left!)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
