"""Effect for Cryofrozen Champion (TIME_613).

Card Text: <b>Deathrattle:</b> Get a random
<b>Legendary</b> minion. Reduce its Cost by (1).
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass