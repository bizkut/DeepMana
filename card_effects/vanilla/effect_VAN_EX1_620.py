"""Effect for Molten Giant (VAN_EX1_620).

Card Text: Costs (1) less for each damage your hero has taken.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass