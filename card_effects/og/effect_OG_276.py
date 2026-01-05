"""Effect for Blood Warriors (OG_276).

Card Text: Add a copy of each damaged friendly minion to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass