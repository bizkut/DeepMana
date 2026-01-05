"""Effect for Parrrley (DED_005).

Card Text: Swap this for a card in your opponent's deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass