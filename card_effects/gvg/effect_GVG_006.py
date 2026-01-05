"""Effect for Mechwarper (GVG_006).

Card Text: Your Mechs cost (1) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass