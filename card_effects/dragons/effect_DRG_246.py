"""Effect for Time Rip (DRG_246).

Card Text: Destroy a minion.
<b>Invoke</b> Galakrond.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()