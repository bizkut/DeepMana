"""Effect for The Leviathan (TSC_030).

Card Text: [x]<b>Colossal +1</b>
<b>Rush</b>, <b>Divine Shield</b>
After this attacks,
<b>Dredge</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1