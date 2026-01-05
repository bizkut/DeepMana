"""Effect for Dark Conviction (ICC_039).

Card Text: Set a minion's Attack and Health to 3.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 3, source)