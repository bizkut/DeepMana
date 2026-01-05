"""Effect for Voidtouched Attendant (SW_446).

Card Text: Both heroes take one extra damage from all sources.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass