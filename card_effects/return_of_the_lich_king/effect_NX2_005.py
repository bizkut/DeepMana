"""Effect for Stitched Creation (NX2_005).

Card Text: <b>Combo:</b> Gain +2/+2.
<b>Infuse ({0}):</b> Gain +3/+3. <b>Manathirst ({1}):</b> Gain +4/+4.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2