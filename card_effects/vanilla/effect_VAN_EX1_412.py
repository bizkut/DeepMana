"""Effect for Raging Worgen (VAN_EX1_412).

Card Text: <b>Enrage:</b> <b>Windfury</b> and +1 Attack
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1