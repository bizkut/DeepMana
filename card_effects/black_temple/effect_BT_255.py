"""Effect for Kael'thas Sunstrider (BT_255).

Card Text: Every third spell you cast each turn costs (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass