"""Effect for Recycle (GVG_031).

Card Text: Shuffle an enemy minion into your opponent's deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass