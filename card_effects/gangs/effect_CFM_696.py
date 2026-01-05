"""Effect for Devolve (CFM_696).

Card Text: Transform all enemy minions into random ones that cost (1) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass