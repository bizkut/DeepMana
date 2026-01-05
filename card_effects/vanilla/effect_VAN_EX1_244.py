"""Effect for Totemic Might (VAN_EX1_244).

Card Text: Give your Totems +2 Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)