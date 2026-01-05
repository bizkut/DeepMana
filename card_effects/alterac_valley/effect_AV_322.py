"""Effect for Snowed In (AV_322).

Card Text: Destroy a damaged minion. <b>Freeze</b> all other minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()