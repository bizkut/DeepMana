"""Effect for Emperor Cobra (VAN_EX1_170).

Card Text: Destroy any minion damaged by this minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()