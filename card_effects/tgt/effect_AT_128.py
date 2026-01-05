"""Effect for The Skeleton Knight (AT_128).

Card Text: <b>Deathrattle:</b> Reveal a minion in each deck. If yours costs more, return this to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass