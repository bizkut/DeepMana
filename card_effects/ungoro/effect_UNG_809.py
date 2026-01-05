"""Effect for Fire Fly (UNG_809).

Card Text: <b>Battlecry</b>: Add a 1/2 Elemental to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass