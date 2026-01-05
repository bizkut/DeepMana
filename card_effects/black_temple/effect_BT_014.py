"""Effect for Starscryer (BT_014).

Card Text: <b>Deathrattle:</b> Draw a spell.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(1)