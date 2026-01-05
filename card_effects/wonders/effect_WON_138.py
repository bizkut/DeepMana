"""Effect for Shark Puncher (WON_138).

Card Text: <b>Deathrattle:</b> Give a random friendly Pirate +2/+2.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2