"""Effect for Convincing Infiltrator (DAL_039).

Card Text: [x]<b><b>Taunt</b></b>
<b>Deathrattle:</b> Destroy a
 random enemy minion.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()