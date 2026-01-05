"""Effect for Rotheart Dryad (EDR_485).

Card Text: <b>Deathrattle:</b> Draw a minion that costs (7) or more.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(7)