"""Effect for Find the Imposter (SW_052).

Card Text: <b>Questline:</b> Play 2
SI:7 cards.
<b>Reward:</b> Add a Spy Gizmo to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass