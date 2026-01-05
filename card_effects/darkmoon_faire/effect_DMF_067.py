"""Effect for Prize Vendor (DMF_067).

Card Text: <b>Battlecry and Deathrattle:</b> Each player draws a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)


def deathrattle(game, source):
    pass