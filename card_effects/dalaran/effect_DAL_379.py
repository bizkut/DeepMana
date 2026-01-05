"""Effect for Vereesa Windrunner (DAL_379).

Card Text: <b>Battlecry:</b> Equip Thori'dal, the Stars' Fury.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass