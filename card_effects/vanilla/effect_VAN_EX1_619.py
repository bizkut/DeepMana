"""Effect for Equality (VAN_EX1_619).

Card Text: Change the Health of ALL minions to 1.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)