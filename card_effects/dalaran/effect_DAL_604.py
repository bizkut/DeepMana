"""Effect for Ursatron (DAL_604).

Card Text: <b>Deathrattle:</b> Draw a Mech from your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(1)