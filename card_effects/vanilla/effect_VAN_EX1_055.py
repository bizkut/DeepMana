"""Effect for Mana Addict (VAN_EX1_055).

Card Text: Whenever you cast a spell, gain +2 Attack this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2