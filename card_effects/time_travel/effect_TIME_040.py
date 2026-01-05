"""Effect for Fading Memory (TIME_040).

Card Text: <b>Deathrattle:</b> Get a
random 5-Cost minion from the past.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass