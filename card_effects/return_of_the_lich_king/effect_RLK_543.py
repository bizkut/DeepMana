"""Effect for Magister's Apprentice (RLK_543).

Card Text: Your Arcane spells
cost (1) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass