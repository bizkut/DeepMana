"""Effect for Sherazin, Corpse Flower (UNG_065).

Card Text: <b>Deathrattle:</b> Go <b>Dormant</b>. Play 4 cards in a turn to revive this minion.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass