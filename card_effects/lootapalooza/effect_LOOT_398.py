"""Effect for Benevolent Djinn (LOOT_398).

Card Text: At the end of your turn, restore #3 Health to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 3, source)