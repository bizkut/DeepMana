"""Effect for Imp King Rafaam (CORE_REV_835).

Card Text: <b>Battlecry:</b> Resurrect
four friendly Imps.
<b>Infuse (5):</b> Give your
Imps +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 5
        target._max_health += 5