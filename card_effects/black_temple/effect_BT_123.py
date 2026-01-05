"""Effect for Kargath Bladefist (BT_123).

Card Text: [x]<b>Rush</b>
<b>Deathrattle:</b> Shuffle
'Kargath Prime'
into your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass