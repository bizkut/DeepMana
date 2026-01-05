"""Effect for Subdue (ULD_728).

Card Text: Set a minion's Attack and Health to 1.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)