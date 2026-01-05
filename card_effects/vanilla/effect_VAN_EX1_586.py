"""Effect for Sea Giant (VAN_EX1_586).

Card Text: Costs (1) less for each other minion on the battlefield.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass