"""Effect for Ozumat (TID_711).

Card Text: [x]<b>Colossal +6</b> 
<b>Deathrattle:</b> For each of
Ozumat's Tentacles, destroy
   a random enemy minion.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()