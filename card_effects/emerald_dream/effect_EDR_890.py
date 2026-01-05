"""Effect for Nightmare Dragonkin (EDR_890).

Card Text: <b>Deathrattle:</b> Reduce the
Cost of the right-most card in your hand by (2).
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass