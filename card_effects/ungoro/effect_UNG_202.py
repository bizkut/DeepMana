"""Effect for Fire Plume Harbinger (UNG_202).

Card Text: <b>Battlecry:</b> Reduce the Cost of Elementals in your hand by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass