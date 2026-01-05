"""Effect for Stormhammer (DRG_007).

Card Text: Doesn't lose Durability while you control a Dragon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass