"""Effect for Astral Rift (BOT_101).

Card Text: Add 2 random minions to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass