"""Effect for Poisoned Blade (AT_034).

Card Text: Your Hero Power gives this +1 Attack instead
of replacing it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1