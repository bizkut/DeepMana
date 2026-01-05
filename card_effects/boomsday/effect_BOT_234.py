"""Effect for Shrink Ray (BOT_234).

Card Text: Set the Attack and Health of all minions
to 1.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)