"""Effect for Regeneratin' Thug (TRL_508).

Card Text: At the start of your turn, restore #2 Health to this minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)