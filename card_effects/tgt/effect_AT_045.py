"""Effect for Aviana (AT_045).

Card Text: Your minions cost (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass