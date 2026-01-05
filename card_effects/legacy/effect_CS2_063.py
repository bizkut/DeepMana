"""Effect for Corruption (CS2_063).

Card Text: Choose an enemy minion. At the start of your turn, destroy it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()