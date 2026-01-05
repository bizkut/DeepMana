"""Effect for Vexallus (RLK_541).

Card Text: Your Arcane spells
cast twice.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass