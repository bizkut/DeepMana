"""Effect for Wailing Vapor (WC_042).

Card Text: [x]After you play an Elemental,
gain +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1