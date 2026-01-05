"""Effect for Humongous Razorleaf (UNG_844).

Card Text: Can't attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass