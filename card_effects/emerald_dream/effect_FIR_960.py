"""Effect for Tending Dragonkin (FIR_960).

Card Text: <b>Battlecry:</b> Copy the lowest Cost Beast in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass