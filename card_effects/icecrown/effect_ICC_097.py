"""Effect for Grave Shambler (ICC_097).

Card Text: Whenever your weapon is destroyed, gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()