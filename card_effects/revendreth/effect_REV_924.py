"""Effect for Primordial Wave (REV_924).

Card Text: [x]Transform enemy minions 
into ones that cost (1) less 
and friendly minions into 
ones that cost (1) more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass