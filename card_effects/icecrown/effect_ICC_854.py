"""Effect for Arfus (ICC_854).

Card Text: [x]<b>Deathrattle:</b> Add a random
<b>Lich King</b> card to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass