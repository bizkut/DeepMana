"""Effect for Apothecary Helbrim (BAR_324).

Card Text: <b>Battlecry and Deathrattle:</b> Add a random Poison to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass