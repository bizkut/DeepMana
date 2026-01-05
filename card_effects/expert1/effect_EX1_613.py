"""Effect for Edwin VanCleef (EX1_613).

Card Text: <b>Combo:</b> Gain +2/+2 for each other card you've played this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2