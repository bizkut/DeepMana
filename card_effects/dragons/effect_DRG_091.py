"""Effect for Shu'ma (DRG_091).

Card Text: At the end of your turn,
fill your board with 1/1 Tentacles.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass