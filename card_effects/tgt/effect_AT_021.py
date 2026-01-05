"""Effect for Tiny Knight of Evil (AT_021).

Card Text: Whenever you discard a card, gain +2/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2