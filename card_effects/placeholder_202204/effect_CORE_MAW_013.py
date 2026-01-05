"""Effect for Life Sentence (CORE_MAW_013).

Card Text: Remove a minion
from the game.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass