"""Effect for Murgur Murgurgle (BT_019).

Card Text: [x]<b>Divine Shield</b>
<b>Deathrattle:</b> Shuffle
'Murgurgle Prime'
into your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass