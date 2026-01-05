"""Effect for Biteweed (UNG_063).

Card Text: <b>Combo:</b> Gain +1/+1 for each other card you've played this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1