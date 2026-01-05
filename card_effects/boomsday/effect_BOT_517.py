"""Effect for Topsy Turvy (BOT_517).

Card Text: Swap a minion's Attack and Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)