"""Effect for Thunder Lizard (UNG_082).

Card Text: <b>Battlecry</b>: If you played an Elemental last turn, <b>Adapt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass