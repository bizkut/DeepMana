"""Effect for Mindgames (VAN_EX1_345).

Card Text: Put a copy of
a random minion from
your opponent's deck into the battlefield.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass