"""Effect for Reliquary Seeker (LOE_116).

Card Text: <b>Battlecry:</b> If you have 6 other minions, gain +4/+4.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 6
        target._max_health += 6