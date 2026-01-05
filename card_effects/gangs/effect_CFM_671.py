"""Effect for Cryomancer (CFM_671).

Card Text: <b>Battlecry:</b> If an enemy is <b>Frozen</b>, gain +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2