"""Effect for Traveling Merchant (SW_307).

Card Text: [x]<b>Tradeable</b>
<b>Battlecry:</b> Gain +1/+1
for each other friendly
 minion you control.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1