"""Effect for Dreaming Drake (YOP_025).

Card Text: <b>Taunt</b>
<b>Corrupt:</b> Gain +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2