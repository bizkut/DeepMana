"""Effect for Metamorfin (SW_451).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> If you've cast a Fel spell this turn, gain +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2