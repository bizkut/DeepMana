"""Effect for Twilight Geomancer (OG_284).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Give your
C'Thun +1/+1 and <b>Taunt</b> <i>(wherever it is)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1