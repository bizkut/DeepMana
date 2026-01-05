"""Effect for Primalfin Challenger (TLC_251).

Card Text: <b>Battlecry:</b> Your next <b>Kindred</b> triggers twice.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass