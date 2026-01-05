"""Effect for Mistwraith (GIL_510).

Card Text: Whenever you play an <b>Echo</b> card, gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1