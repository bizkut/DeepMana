"""Effect for Tentacles for Arms (OG_033).

Card Text: <b>Deathrattle:</b> Return this to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass