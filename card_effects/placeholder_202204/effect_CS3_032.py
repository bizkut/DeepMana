"""Effect for Onyxia the Broodmother (CS3_032).

Card Text: At the end of each turn, fill your board with 1/1 Whelps.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass