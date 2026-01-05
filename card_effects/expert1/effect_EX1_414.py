"""Effect for Grommash Hellscream (EX1_414).

Card Text: <b>Charge</b>
Has +6 Attack while damaged.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 6
        target._max_health += 6