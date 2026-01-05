"""Effect for Convert (AT_015).

Card Text: Put a copy of an enemy minion into your hand. It costs (1).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass