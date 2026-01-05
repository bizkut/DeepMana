"""Effect for Pterrordax Hatchling (UNG_001).

Card Text: <b><b>Battlecry:</b> Adapt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass