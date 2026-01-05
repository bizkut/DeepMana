"""Effect for Reforestation (EDR_843).

Card Text: [x]<b>Choose One -</b> Draw a
spell; or Draw a minion.
<i>(Hold this for 3 turns
to do both!)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)