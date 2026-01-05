"""Effect for Gorehowl (CORE_EX1_411).

Card Text: Attacking a minion costs 1 Attack instead of 1 Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass