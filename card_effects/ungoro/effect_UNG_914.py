"""Effect for Raptor Hatchling (UNG_914).

Card Text: <b>Deathrattle:</b> Shuffle a 4/5 Raptor into your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass