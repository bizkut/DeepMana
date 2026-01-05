"""Effect for Gruul (NEW1_038).

Card Text: At the end of each turn, gain +1/+1 .
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1