"""Effect for Vicious Slitherspear (CORE_TSC_827).

Card Text: [x]After you cast a spell,
gain +1 Attack until
your next turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1