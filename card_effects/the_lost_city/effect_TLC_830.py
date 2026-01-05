"""Effect for The Food Chain (TLC_830).

Card Text: <b>Quest:</b> Play a 1, 3, 5, and 7-Attack Beast.
<b>Reward:</b> Shokk.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass