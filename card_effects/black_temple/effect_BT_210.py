"""Effect for Zixor, Apex Predator (BT_210).

Card Text: [x]<b>Rush</b>
<b>Deathrattle:</b> Shuffle 'Zixor
Prime' into your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass