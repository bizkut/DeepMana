"""Effect for Ur'zul Horror (BT_407).

Card Text: <b>Deathrattle:</b> Add a 2/1 Lost Soul to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass