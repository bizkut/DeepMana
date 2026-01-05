"""Effect for Murloc Tastyfin (TRL_520).

Card Text: [x]<b>Deathrattle:</b> Draw 2 Murlocs
from your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(2)