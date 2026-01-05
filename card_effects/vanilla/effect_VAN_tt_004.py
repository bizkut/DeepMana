"""Effect for Flesheating Ghoul (VAN_tt_004).

Card Text: Whenever a minion dies, gain +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1