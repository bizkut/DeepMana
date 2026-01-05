"""Effect for Witchwood Apple (GIL_663).

Card Text: Add two 2/2 Treants to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass