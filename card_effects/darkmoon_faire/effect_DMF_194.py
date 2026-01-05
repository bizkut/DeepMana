"""Effect for Redscale Dragontamer (DMF_194).

Card Text: <b>Deathrattle:</b> Draw a Dragon.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(1)