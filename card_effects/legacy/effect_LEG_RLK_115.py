"""Effect for Repulsive Gargantuan (LEG_RLK_115).

Card Text: Enemy characters
can't be healed.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)