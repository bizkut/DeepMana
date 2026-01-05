"""Effect for Forlorn Stalker (OG_292).

Card Text: <b>Battlecry:</b> Give all <b>Deathrattle</b> minions in your hand +1/+1.
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