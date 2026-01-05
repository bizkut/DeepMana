"""Effect for Oh My Yogg! (DMF_236).

Card Text: [x]<b>Secret:</b> When your
opponent casts a spell,
they instead cast a random
one of the same Cost.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass