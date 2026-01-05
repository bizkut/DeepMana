"""Effect for Redband Wasp (GIL_155).

Card Text: <b>Rush</b>
Has +3 Attack while damaged.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3