"""Effect for Bamboozle (BT_042).

Card Text: [x]<b>Secret:</b> When one of
your minions is attacked,
transform it into a random
one that costs (3) more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass