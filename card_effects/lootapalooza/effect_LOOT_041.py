"""Effect for Kobold Barbarian (LOOT_041).

Card Text: At the start of your turn, attack a random enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass