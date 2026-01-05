"""Effect for Luckydo Buccaneer (CFM_342).

Card Text: <b>Battlecry:</b> If your weapon has at least 3 Attack, gain +4/+4.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3