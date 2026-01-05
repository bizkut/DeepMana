"""Effect for Rhonin (AT_009).

Card Text: <b>Deathrattle:</b> Add 3 copies of Arcane Missiles to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass