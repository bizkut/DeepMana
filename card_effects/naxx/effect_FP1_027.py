"""Effect for Stoneskin Gargoyle (FP1_027).

Card Text: At the start of your turn, restore this minion to full Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)