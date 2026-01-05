"""Effect for Alternate Reality (TIME_707).

Card Text: [x]Replace your hand and
deck with random <b>Choose
One</b> cards from the past.
They cost (1) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass