"""Effect for King Mukla (VAN_EX1_014).

Card Text: <b>Battlecry:</b> Give your opponent 2 Bananas.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2