"""Effect for Truesilver Champion (VAN_CS2_097).

Card Text: Whenever your hero attacks, restore #2 Health to it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)