"""Effect for Curious Explorer (TLC_244).

Card Text: [x]<b>Deathrattle:</b> Reduce the
Cost of a minion in your
 opponent's hand by (2).
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass