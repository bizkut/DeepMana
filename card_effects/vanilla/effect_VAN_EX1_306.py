"""Effect for Felstalker (VAN_EX1_306).

Card Text: <b>Battlecry:</b> Discard a random card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass