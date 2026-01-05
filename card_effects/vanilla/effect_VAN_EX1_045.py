"""Effect for Ancient Watcher (VAN_EX1_045).

Card Text: Can't attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass