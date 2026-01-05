"""Effect for Circle of Healing (EX1_621).

Card Text: Restore #4 Health to ALL minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 4, source)