"""Effect for Violet Haze (BOT_084).

Card Text: Add 2 random <b>Deathrattle</b> cards to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass