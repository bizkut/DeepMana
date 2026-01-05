"""Effect for Fleethoof Pearltusk (DMF_080).

Card Text: <b>Rush</b>
<b>Corrupt:</b> Gain +4/+4.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4