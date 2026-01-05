"""Effect for From the Depths (TSC_940).

Card Text: [x]Reduce the Cost of the
bottom five cards in your
 deck by (3), then <b>Dredge</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass