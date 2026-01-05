"""Effect for Tainted Zealot (ICC_913).

Card Text: <b>Divine Shield</b>
<b>Spell Damage +1</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1