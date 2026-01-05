"""Effect for Rotgill (RLK_550).

Card Text: [x]<b>Battlecry:</b> Give your other
minions "<b>Deathrattle:</b> Give
  your minions +1/+1."
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