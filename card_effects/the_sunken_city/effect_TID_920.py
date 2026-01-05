"""Effect for Drown (TID_920).

Card Text: Put an enemy minion on the bottom of your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass