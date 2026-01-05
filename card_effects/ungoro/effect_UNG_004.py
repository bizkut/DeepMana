"""Effect for Dinosize (UNG_004).

Card Text: Set a minion's stats to 7/14.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass