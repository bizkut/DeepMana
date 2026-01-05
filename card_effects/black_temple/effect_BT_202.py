"""Effect for Helboar (BT_202).

Card Text: <b>Deathrattle:</b> Give a random Beast in your hand +1/+1.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1