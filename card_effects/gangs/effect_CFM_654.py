"""Effect for Friendly Bartender (CFM_654).

Card Text: At the end of your turn, restore #1 Health to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)