"""Effect for Ghoulish Alchemist (RLK_570).

Card Text: <b>Battlecry</b>: Your next Concoction costs (0).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass