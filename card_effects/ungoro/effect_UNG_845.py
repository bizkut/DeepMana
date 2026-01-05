"""Effect for Igneous Elemental (UNG_845).

Card Text: <b>Deathrattle:</b> Add two 1/2 Flame Elementals to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass