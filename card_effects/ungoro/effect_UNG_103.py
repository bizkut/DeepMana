"""Effect for Evolving Spores (UNG_103).

Card Text: <b>Adapt</b> your minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass