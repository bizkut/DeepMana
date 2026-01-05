"""Effect for Gentle Megasaur (UNG_089).

Card Text: <b>Battlecry:</b> <b>Adapt</b> your Murlocs.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass