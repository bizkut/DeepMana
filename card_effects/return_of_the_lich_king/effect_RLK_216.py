"""Effect for Rotten Rodent (RLK_216).

Card Text: <b>Battlecry:</b> Reduce the Cost of all <b>Deathrattle</b> cards in your deck by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass