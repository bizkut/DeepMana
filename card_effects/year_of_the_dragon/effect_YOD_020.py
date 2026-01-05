"""Effect for Explosive Evolution (YOD_020).

Card Text: Transform a minion into a random one that costs (3) more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass