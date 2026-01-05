"""Effect for Meanstreet Marshal (CFM_759).

Card Text: <b>Deathrattle:</b> If this minion has 2 or more Attack, draw a card.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(2)