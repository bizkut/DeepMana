"""Effect for Ramkahen Wildtamer (ULD_151).

Card Text: <b>Battlecry:</b> Copy a random Beast in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass