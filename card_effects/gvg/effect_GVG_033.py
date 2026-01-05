"""Effect for Tree of Life (GVG_033).

Card Text: Restore all characters to full Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)