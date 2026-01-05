"""Effect for Chum Bucket (TSC_957).

Card Text: [x]Give all Murlocs in your
hand +1/+1. Repeat for
each Murloc you control.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1