"""Effect for Cannibalize (NX2_020).

Card Text: Destroy a minion. Restore its Health to all friendly characters.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()