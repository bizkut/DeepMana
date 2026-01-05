"""Effect for Cutlass Courier (TSC_085).

Card Text: After your hero attacks, draw a Pirate.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)