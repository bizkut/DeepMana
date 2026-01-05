"""Effect for Witch's Brew (DAL_432).

Card Text: Restore #4 Health. Repeatable this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 4, source)