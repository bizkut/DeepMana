"""Effect for The Last Kaleidosaur (UNG_954).

Card Text: <b>Quest:</b> Cast 5 spells
on your minions.
<b>Reward:</b> Galvadon.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass