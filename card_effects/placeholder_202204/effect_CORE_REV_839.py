"""Effect for Sinstone Totem (CORE_REV_839).

Card Text: At the end of your turn, gain +1 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)