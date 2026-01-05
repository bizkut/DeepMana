"""Effect for Anubisath Sentinel (LOE_061).

Card Text: <b>Deathrattle:</b> Give a random friendly minion +3/+3.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3