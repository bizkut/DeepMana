"""Effect for Tranquil Treant (EDR_861).

Card Text: <b>Deathrattle:</b> Both
players gain an empty Mana Crystal.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass