"""Effect for Murloc Warleader (VAN_EX1_507).

Card Text: ALL other murlocs have +2/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2