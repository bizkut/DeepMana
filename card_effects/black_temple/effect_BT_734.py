"""Effect for Supreme Abyssal (BT_734).

Card Text: Can't attack heroes.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass