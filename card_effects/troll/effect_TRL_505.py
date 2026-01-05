"""Effect for Helpless Hatchling (TRL_505).

Card Text: <b>Deathrattle:</b> Reduce the Cost of a Beast in your hand by (1).
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass