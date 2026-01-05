"""Effect for Kabal Outfitter (BAR_915).

Card Text: [x]<b>Battlecry and Deathrattle:</b>
Give another random
 friendly minion +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1


def deathrattle(game, source):
    pass