"""Effect for Horrendous Growth (DMF_124).

Card Text: <b>Corrupt:</b> Gain +1/+1. Can be <b>Corrupted</b> endlessly.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1