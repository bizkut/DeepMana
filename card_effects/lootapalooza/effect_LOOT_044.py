"""Effect for Bladed Gauntlet (LOOT_044).

Card Text: Has Attack equal to your Armor. Can't attack heroes.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass