"""Effect for Woodcutter's Axe (CORE_GIL_653).

Card Text: <b>Deathrattle:</b> Give +2/+1 to a random friendly minion.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2