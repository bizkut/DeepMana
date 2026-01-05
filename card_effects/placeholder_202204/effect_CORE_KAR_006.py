"""Effect for Cloaked Huntress (CORE_KAR_006).

Card Text: Your <b>Secrets</b> cost (0).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass