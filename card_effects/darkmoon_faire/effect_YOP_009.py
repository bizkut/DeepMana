"""Effect for Rally! (YOP_009).

Card Text: Resurrect a friendly
1-Cost, 2-Cost, and
3-Cost minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass