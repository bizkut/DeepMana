"""Effect for Twisted Treant (EDR_495).

Card Text: <b>Deathrattle:</b> Give a random minion in each player's hand -2 Attack.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2