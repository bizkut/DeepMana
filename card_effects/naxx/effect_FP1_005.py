"""Effect for Shade of Naxxramas (FP1_005).

Card Text: <b><b>Stealth</b>.</b> At the start of your turn, gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1