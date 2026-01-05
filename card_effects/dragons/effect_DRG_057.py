"""Effect for Hot Air Balloon (DRG_057).

Card Text: At the start of your turn, gain +1 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)