"""Effect for Ebon Dragonsmith (LOOT_118).

Card Text: <b>Battlecry:</b> Reduce the Cost of a random weapon in your hand by (2).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass