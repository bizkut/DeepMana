"""Effect for Polluted Hoarder (OG_323).

Card Text: <b>Deathrattle:</b> Draw a card.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(1)