"""Effect for Nerubian Prophet (OG_138).

Card Text: At the start of your turn, reduce this card's
Cost by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass