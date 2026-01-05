"""Effect for Ramming Speed (DRG_022).

Card Text: Force a minion to attack one of its neighbors.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass