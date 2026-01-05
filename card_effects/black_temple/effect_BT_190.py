"""Effect for Replicat-o-tron (BT_190).

Card Text: At the end of your turn, transform a neighbor into a copy of this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass