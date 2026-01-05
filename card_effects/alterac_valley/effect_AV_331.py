"""Effect for Najak Hexxen (AV_331).

Card Text: [x]<b>Battlecry:</b> Take control of
an enemy minion.
<b>Deathrattle:</b> Give the
minion back.
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