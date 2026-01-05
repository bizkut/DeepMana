"""Effect for Arcsplitter (RLK_542).

Card Text: <b>Deathrattle:</b> Add 2 Arcane Bolts to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass