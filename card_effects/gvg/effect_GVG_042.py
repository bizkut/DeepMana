"""Effect for Neptulon (GVG_042).

Card Text: <b>Battlecry:</b> Add 4 random Murlocs to your hand. <b>Overload:</b> (3)
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass