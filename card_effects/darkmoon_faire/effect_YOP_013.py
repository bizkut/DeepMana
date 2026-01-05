"""Effect for Spiked Wheel (YOP_013).

Card Text: Has +3 Attack while your hero has Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3