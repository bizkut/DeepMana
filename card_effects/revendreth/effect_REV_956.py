"""Effect for Priest of the Deceased (REV_956).

Card Text: <b>Taunt</b>
<b>Infuse (3):</b> Gain +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3