"""Effect for Mechanized Magma (TLC_224).

Card Text: Whenever you play a
Fire spell, gain stats
equal to its Cost.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass