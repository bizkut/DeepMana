"""Effect for Night Prowler (GIL_624).

Card Text: <b>Battlecry:</b> If this is the only minion on the battlefield, gain +3/+3.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3