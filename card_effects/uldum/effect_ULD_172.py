"""Effect for Plague of Murlocs (ULD_172).

Card Text: Transform all minions into random Murlocs.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass