"""Effect for Runic Egg (KAR_029).

Card Text: <b>Deathrattle:</b> Draw a card.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(1)