"""Effect for Summoning Portal (VAN_EX1_315).

Card Text: Your minions cost (2) less, but not less than (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass