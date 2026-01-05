"""Effect for Nerub'ar Weblord (FP1_017).

Card Text: Minions with <b>Battlecry</b> cost (2) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass