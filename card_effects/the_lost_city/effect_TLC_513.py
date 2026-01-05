"""Effect for Lie in Wait (TLC_513).

Card Text: [x]<b>Quest:</b> Shuffle cards
into your deck, 5 times.
<b>Reward: </b>Master Dusk.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass