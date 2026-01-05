"""Effect for Reliquary of Souls (BT_197).

Card Text: [x]<b>Lifesteal</b>
<b>Deathrattle:</b> Shuffle
'Reliquary Prime'
into your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass