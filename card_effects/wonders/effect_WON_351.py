"""Effect for Small-Time Buccaneer (WON_351).

Card Text: Has +2 Attack while you have a weapon equipped.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2