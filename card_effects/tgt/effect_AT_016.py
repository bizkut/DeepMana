"""Effect for Confuse (AT_016).

Card Text: Swap the Attack and Health of all minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)