"""Effect for Flesh Giant (SCH_140).

Card Text: Costs (1) less for each time your hero's Health changed during your turns.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)