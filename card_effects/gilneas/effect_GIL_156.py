"""Effect for Quartz Elemental (GIL_156).

Card Text: Can't attack while damaged.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass