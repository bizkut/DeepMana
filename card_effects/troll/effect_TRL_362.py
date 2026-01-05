"""Effect for Dragon Roar (TRL_362).

Card Text: Add 2 random Dragons to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass