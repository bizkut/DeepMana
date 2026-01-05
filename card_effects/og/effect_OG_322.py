"""Effect for Blackwater Pirate (OG_322).

Card Text: Your weapons cost (2) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass