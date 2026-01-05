"""Effect for Naga Sea Witch (LOE_038).

Card Text: Your cards cost (5).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass