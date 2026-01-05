"""Effect for Divergence (TIME_030).

Card Text: Split a random
minion in your hand into two halves.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass