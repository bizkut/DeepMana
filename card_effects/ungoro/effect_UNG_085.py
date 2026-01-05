"""Effect for Emerald Hive Queen (UNG_085).

Card Text: Your minions cost (2) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass