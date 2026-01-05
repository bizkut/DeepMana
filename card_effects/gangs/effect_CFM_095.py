"""Effect for Weasel Tunneler (CFM_095).

Card Text: <b>Deathrattle:</b> Shuffle this minion into your opponent's deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass