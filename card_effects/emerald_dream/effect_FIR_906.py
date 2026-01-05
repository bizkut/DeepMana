"""Effect for Overheat (FIR_906).

Card Text: Give your minions +1/+1. Discard a random Nature spell to give them +1/+1 more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1