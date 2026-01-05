"""Effect for Clutchmother Zavas (UNG_836).

Card Text: Whenever you discard this, give it +2/+2 and return it to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2