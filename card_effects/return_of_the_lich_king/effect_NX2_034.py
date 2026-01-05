"""Effect for Rivendare, Warrider (NX2_034).

Card Text: <b>Deathrattle:</b> Shuffle the other 3 Horsemen into your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass