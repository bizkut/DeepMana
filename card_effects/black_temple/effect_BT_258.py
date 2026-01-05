"""Effect for Imprisoned Homunculus (BT_258).

Card Text: <b>Dormant</b> for 2 turns.
<b>Taunt</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass