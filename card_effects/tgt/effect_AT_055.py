"""Effect for Flash Heal (AT_055).

Card Text: Restore #5 Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 5, source)