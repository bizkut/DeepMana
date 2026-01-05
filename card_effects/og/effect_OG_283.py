"""Effect for C'Thun's Chosen (OG_283).

Card Text: [x]<b>Divine Shield</b>
<b>Battlecry:</b> Give your C'Thun
+3/+3 <i>(wherever it is).</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3