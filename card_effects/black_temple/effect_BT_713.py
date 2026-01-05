"""Effect for Akama (BT_713).

Card Text: [x]<b>Stealth</b>
<b>Deathrattle:</b> Shuffle 'Akama
Prime' into your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass