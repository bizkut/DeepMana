"""Effect for Tortotem (DINO_412).

Card Text: [x]At the end of your turn,
get a random minion with
multiple minion types.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass