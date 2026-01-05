"""Effect for Malorne (WON_011).

Card Text: <b>Deathrattle:</b> Go <b>Dormant</b>. Revive after 2 friendly Beasts die.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass