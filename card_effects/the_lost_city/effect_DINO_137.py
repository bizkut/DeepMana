"""Effect for Skittish Saucier (DINO_137).

Card Text: <b>Battlecry:</b> Reduce the Cost of adjacent cards in
your hand by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass