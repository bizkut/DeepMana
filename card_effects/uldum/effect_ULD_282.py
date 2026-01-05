"""Effect for Jar Dealer (ULD_282).

Card Text: [x]<b>Deathrattle:</b> Add a random
1-Cost minion to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass