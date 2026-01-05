"""Effect for Snap Freeze (GIL_801).

Card Text: <b>Freeze</b> a minion.
If it's already <b>Frozen</b>, destroy it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()