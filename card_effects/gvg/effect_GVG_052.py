"""Effect for Crush (GVG_052).

Card Text: Destroy a minion. If you have a damaged minion, this costs (4) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()