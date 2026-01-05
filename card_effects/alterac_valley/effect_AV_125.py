"""Effect for Tower Sergeant (AV_125).

Card Text: <b>Battlecry:</b> If you control at least 2 other minions, gain +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2