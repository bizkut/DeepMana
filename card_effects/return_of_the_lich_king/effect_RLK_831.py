"""Effect for Plaguespreader (RLK_831).

Card Text: <b>Deathrattle:</b> Transform a random minion in your opponent's hand into a Plaguespreader.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass