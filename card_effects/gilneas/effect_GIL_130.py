"""Effect for Gloom Stag (GIL_130).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> If your deck has only odd-Cost cards, gain +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2