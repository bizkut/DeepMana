"""Effect for Dreambound Disciple (EDR_847).

Card Text: <b>Battlecry and Deathrattle:</b> Your next Hero Power costs (0).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass