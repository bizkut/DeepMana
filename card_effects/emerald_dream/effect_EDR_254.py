"""Effect for Animated Moonwell (EDR_254).

Card Text: After you cast a spell, gain Attack equal to its Cost.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass