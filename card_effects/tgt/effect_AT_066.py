"""Effect for Orgrimmar Aspirant (AT_066).

Card Text: <b>Inspire:</b> Give your weapon +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1