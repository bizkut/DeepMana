"""Effect for Mark of Ursol (EDR_252).

Card Text: [x]Choose a minion. If it's
an enemy, set its stats
to 1/1. If it's friendly, set
its stats to 3/3 instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass