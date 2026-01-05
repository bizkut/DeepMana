"""Effect for Pick Pocket (GIL_696).

Card Text: <b>Echo</b>
Add a random card to your hand <i>(from your opponent's class).</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass