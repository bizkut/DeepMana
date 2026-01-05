"""Effect for Volcanosaur (UNG_002).

Card Text: <b>Battlecry:</b> <b>Adapt</b>, then <b>Adapt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass