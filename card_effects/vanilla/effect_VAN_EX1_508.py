"""Effect for Grimscale Oracle (VAN_EX1_508).

Card Text: ALL other Murlocs have +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1