"""Effect for Time-Lost Glaive (TIME_444).

Card Text: <b>Deathrattle:</b> Get a random Demon
from the past.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass