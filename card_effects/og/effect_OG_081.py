"""Effect for Shatter (OG_081).

Card Text: Destroy a <b>Frozen</b> minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()