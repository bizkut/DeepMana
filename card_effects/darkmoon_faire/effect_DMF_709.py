"""Effect for Grand Totem Eys'or (DMF_709).

Card Text: At the end of your turn,
give +1/+1 to all other Totems in your hand, deck and battlefield.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1