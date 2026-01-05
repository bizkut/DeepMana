"""Effect for Nofin Can Stop Us (BAR_041).

Card Text: [x]Give your minions
+1/+1. Give your
Murlocs an extra +1/+1.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1