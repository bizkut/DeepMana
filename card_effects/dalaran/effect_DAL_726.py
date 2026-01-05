"""Effect for Scargil (DAL_726).

Card Text: Your Murlocs cost (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass