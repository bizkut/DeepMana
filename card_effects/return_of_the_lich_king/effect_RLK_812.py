"""Effect for Animate Dead (RLK_812).

Card Text: Resurrect a friendly minion that costs (3)
or less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass