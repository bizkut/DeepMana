"""Effect for Spirit of the Mountain (TLC_229).

Card Text: <b>Quest:</b> Play 6 minions
of unique types.
<b>Reward:</b> Ashalon.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass