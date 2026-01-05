"""Effect for Lightfused Stegodon (UNG_962).

Card Text: <b>Battlecry:</b> <b>Adapt</b> your Silver Hand Recruits.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass