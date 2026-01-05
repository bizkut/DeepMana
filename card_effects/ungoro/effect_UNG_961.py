"""Effect for Adaptation (UNG_961).

Card Text: <b>Adapt</b> a friendly minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass