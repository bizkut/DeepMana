"""Effect for Azsharan Defector (TSC_057).

Card Text: [x]<b>Rush</b>. <b>Deathrattle:</b> Put a
'Sunken Defector' on the 
bottom of your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass