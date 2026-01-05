"""Effect for Spiteful Smith (CS2_221).

Card Text: Your weapon has +2 Attack while this is damaged.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2