"""Effect for Umbral Geist (RLK_914).

Card Text: [x]<b>Deathrattle:</b> Add a random
Shadow spell to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass