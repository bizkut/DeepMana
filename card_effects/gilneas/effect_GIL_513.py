"""Effect for Lost Spirit (GIL_513).

Card Text: <b>Deathrattle:</b> Give your minions +1 Attack.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1