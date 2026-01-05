"""Effect for Calamity's Grasp (NX2_025).

Card Text: <b>Deathrattle:</b> Add a random <b>Outcast</b> card to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass