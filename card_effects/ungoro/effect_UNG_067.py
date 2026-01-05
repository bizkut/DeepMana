"""Effect for The Caverns Below (UNG_067).

Card Text: [x]<b>Quest:</b> Play four minions
with the same name.
<b>Reward:</b> Crystal Core.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass