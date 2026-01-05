"""Effect for Healing Touch (CS2_007).

Card Text: Restore #8 Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 8, source)