"""Effect for Divine Hymn (GIL_661).

Card Text: Restore #6 Health to all friendly characters.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 6, source)