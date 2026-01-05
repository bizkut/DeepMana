"""Effect for Sahket Sapper (ULD_280).

Card Text: <b>Deathrattle:</b> Return a  random enemy minion to  your opponent's hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass