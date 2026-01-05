"""Effect for Molten Giant (CORE_EX1_620).

Card Text: Costs (1) less for
each Health your hero
is missing.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)