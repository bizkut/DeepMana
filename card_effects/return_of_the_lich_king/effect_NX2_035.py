"""Effect for Rimescale Siren (NX2_035).

Card Text: [x]<b>Battlecry:</b> If you've cast three
spells while holding this,
<b>Freeze</b> 3 random enemy
minions.@ <i>({0} left!)</i>@ <i>(Ready!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.frozen = True