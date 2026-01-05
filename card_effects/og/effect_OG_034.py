"""Effect for Silithid Swarmer (OG_034).

Card Text: Can only attack if your hero attacked this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass