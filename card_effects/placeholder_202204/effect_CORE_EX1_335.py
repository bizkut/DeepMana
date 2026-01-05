"""Effect for Lightspawn (CORE_EX1_335).

Card Text: This minion's Attack is always equal to its Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)