"""Effect for Jeeves (GVG_094).

Card Text: At the end of each player's turn, that player draws until they have 3 cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)