"""Effect for Molten Blade (UNG_929).

Card Text: Transforms into a new weapon when in hand that changes each turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass