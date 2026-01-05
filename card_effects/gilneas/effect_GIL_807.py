"""Effect for Bogshaper (GIL_807).

Card Text: Whenever you cast a spell, draw a minion from your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)