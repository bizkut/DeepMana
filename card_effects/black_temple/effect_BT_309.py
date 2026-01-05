"""Effect for Kanrethad Ebonlocke (BT_309).

Card Text: [x]Your Demons cost (1) less.
<b>Deathrattle:</b> Shuffle
'Kanrethad Prime'
into your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass