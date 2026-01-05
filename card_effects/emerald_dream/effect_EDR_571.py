"""Effect for Fae Trickster (EDR_571).

Card Text: <b>Deathrattle:</b> Draw a spell that costs (5) or more.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(5)