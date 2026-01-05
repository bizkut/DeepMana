"""Effect for Coldarra Drake (AT_008).

Card Text: You can use your Hero Power any number of times.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass