"""Effect for Waggle Pick (DAL_720).

Card Text: [x]<b>Deathrattle:</b> Return
a random friendly
minion to your hand.
It costs (2) less.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass