"""Effect for Baron Rivendare (CORE_FP1_031).

Card Text: Your minions trigger their <b>Deathrattles</b> twice.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass