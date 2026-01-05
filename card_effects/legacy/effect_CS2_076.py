"""Effect for Assassinate (CS2_076).

Card Text: Destroy an enemy minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()