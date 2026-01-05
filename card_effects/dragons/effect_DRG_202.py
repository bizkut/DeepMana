"""Effect for Dragonblight Cultist (DRG_202).

Card Text: [x]<b>Battlecry:</b> <b>Invoke</b> Galakrond.
Gain +1 Attack for each
other friendly minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1