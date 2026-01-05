"""Effect for Burgle (WON_071).

Card Text: Get 3 random
cards <i>(from your
opponent's class)</i>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass