"""Effect for Unstable Portal (GVG_003).

Card Text: Add a random minion to your hand. It costs (3) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass