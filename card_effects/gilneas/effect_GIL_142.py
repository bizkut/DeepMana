"""Effect for Chameleos (GIL_142).

Card Text: Each turn this is in your hand, transform it into a card your opponent is holding.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass