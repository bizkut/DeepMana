"""Effect for Creepy Painting (CORE_REV_916).

Card Text: After another minion dies, become a copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass