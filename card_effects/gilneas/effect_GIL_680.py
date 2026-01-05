"""Effect for Walnut Sprite (GIL_680).

Card Text: <b>Echo</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass