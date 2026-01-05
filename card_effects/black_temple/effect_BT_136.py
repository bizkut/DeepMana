"""Effect for Archspore Msshi'fn (BT_136).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Shuffle
'Msshi'fn Prime'
into your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass