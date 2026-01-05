"""Effect for Holy Maki Roll (TSC_952).

Card Text: Restore #2 Health. Repeatable this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)