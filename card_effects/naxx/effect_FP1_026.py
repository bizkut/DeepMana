"""Effect for Anub'ar Ambusher (FP1_026).

Card Text: <b>Deathrattle:</b> Return a random friendly minion to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass