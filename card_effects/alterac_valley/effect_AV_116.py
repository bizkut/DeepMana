"""Effect for Arcane Brilliance (AV_116).

Card Text: Add a copy of a 7, 8, 9, and 10-Cost spell in your deck to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass