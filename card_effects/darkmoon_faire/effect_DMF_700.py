"""Effect for Revolve (DMF_700).

Card Text: Transform all minions into random ones with the same Cost.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass