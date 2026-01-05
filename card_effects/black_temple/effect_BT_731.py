"""Effect for Infectious Sporeling (BT_731).

Card Text: After this damages a minion, turn it into an Infectious Sporeling.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass