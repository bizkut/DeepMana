"""Effect for Silence (VAN_EX1_332).

Card Text: <b>Silence</b> a minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.silence(target)