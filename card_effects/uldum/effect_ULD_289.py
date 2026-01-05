"""Effect for Fishflinger (ULD_289).

Card Text: <b>Battlecry:</b> Add a
random Murloc to each player's hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass