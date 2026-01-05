"""Effect for Semi-Stable Portal (TIME_000).

Card Text: <b>Rewind</b>
Add a random minion
to your hand. It costs
(3) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass