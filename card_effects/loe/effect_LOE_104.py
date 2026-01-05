"""Effect for Entomb (LOE_104).

Card Text: Choose an enemy minion.
Shuffle it into your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass