"""Effect for Mutate (DAL_071).

Card Text: Transform a friendly minion into a random one that costs (1) more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass