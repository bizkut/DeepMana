"""Effect for Shallow Gravedigger (ICC_702).

Card Text: <b>Deathrattle:</b> Add a random <b>Deathrattle</b> minion to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass