"""Effect for Verdant Longneck (UNG_100).

Card Text: <b>Battlecry:</b> <b>Adapt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass