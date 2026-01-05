"""Effect for Daring Drake (RLK_916).

Card Text: [x]<b>Rush</b>
<b>Battlecry:</b> If you're holding
a Dragon, gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1