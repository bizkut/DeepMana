"""Effect for Corridor Creeper (LOOT_149).

Card Text: Costs (1) less whenever a minion dies while this is in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass