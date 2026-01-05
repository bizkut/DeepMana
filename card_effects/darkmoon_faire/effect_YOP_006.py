"""Effect for Hysteria (YOP_006).

Card Text: [x]Choose an enemy minion.
It attacks random
minions until it dies.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass