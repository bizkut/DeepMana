"""Effect for Jackpot! (TID_931).

Card Text: Add two random
spells from other classes
that cost (5) or more
to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass