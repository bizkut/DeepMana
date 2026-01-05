"""Effect for Titanographer Osk (TLC_452).

Card Text: Gains a random <b>Titan</b> ability in your hand that changes each turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass