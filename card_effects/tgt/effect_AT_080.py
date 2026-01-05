"""Effect for Garrison Commander (AT_080).

Card Text: You can use your Hero Power twice a turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass