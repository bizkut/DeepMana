"""Effect for Bonedigger Geist (RLK_753).

Card Text: <b>Battlecry:</b> Spend a <b>Corpse</b> to gain +1/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1