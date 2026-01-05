"""Effect for Scourge Troll (RLK_912).

Card Text: <b>Deathrattles</b> given to this minion trigger twice.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1