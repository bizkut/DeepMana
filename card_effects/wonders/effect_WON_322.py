"""Effect for Usher of Souls (WON_322).

Card Text: Whenever a minion dies, give your C'Thun +1/+1
<i>(wherever it is).</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1