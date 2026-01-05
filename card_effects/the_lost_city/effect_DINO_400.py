"""Effect for Barricade Basher (DINO_400).

Card Text: [x]Whenever you gain Armor,
 gain +2/+2 and attack a
random enemy minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2