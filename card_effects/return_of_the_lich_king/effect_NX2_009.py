"""Effect for Cold Storage (NX2_009).

Card Text: <b>Freeze</b> a minion. Add a copy of it to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.frozen = True