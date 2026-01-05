"""Effect for Story of the Waygate (TLC_364).

Card Text: [x]Reduce the Cost of cards
in your hand that didn't
start in your deck by (1).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass