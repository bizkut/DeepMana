"""Effect for Unbound Elemental (EX1_258).

Card Text: After you play a card with <b>Overload</b>, gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1