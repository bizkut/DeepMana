"""Effect for Bloodseeker (AV_244).

Card Text: <b>Honorable Kill:</b>
Gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1