"""Effect for Duplicate (FP1_018).

Card Text: <b>Secret:</b> When a friendly minion dies, put 2 copies of it into your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass