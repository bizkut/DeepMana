"""Effect for Crystalline Oracle (UNG_032).

Card Text: [x]<b>Deathrattle:</b> Copy a card
from your opponent's deck
 and add it to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass