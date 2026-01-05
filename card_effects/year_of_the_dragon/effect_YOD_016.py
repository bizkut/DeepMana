"""Effect for Skyvateer (YOD_016).

Card Text: <b>Stealth</b>
<b>Deathrattle:</b> Draw a card.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(1)