"""Effect for Unstable Evolution (LOOT_504).

Card Text: <b>Echo</b>
Transform a friendly minion into one that costs (1) more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass