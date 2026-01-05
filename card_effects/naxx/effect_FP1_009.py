"""Effect for Deathlord (FP1_009).

Card Text: <b>Taunt. Deathrattle:</b> Your opponent puts a minion from their deck into the battlefield.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass