"""Effect for Primalfin Champion (UNG_953).

Card Text: [x]<b>Deathrattle:</b> Return any
spells you cast on this
minion to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass