"""Effect for Flustered Librarian (CORE_REV_242).

Card Text: Has +1 Attack for each
Imp you control.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1