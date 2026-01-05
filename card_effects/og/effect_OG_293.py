"""Effect for Dark Arakkoa (OG_293).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> Give your C'Thun
+4/+4 <i>(wherever it is).</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4