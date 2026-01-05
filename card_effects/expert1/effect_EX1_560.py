"""Effect for Nozdormu (EX1_560).

Card Text: Players only have 15 seconds to take their turns.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass