"""Effect for Lightwell (VAN_EX1_341).

Card Text: At the start of your turn, restore #3 Health to a damaged friendly character.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 3, source)