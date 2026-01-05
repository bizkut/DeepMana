"""Effect for Gang Up (BRM_007).

Card Text: Choose a minion. Shuffle 3 copies of it into your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass