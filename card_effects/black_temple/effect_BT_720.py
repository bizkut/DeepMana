"""Effect for Ruststeed Raider (BT_720).

Card Text: <b>Taunt</b>, <b>Rush</b>
<b>Battlecry:</b> Gain +4 Attack this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4