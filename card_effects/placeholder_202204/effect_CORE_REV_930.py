"""Effect for Crazed Wretch (CORE_REV_930).

Card Text: Has +2 Attack and <b>Charge</b> while damaged.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2