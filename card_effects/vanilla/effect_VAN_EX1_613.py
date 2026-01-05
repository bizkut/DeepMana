"""Effect for Edwin VanCleef (VAN_EX1_613).

Card Text: <b>Combo:</b> Gain +2/+2 for each card played earlier this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2