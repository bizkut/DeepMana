"""Effect for Hobart Grapplehammer (CFM_643).

Card Text: [x]<b>Battlecry:</b> If you have a
weapon equipped, give
all minions in your hand
and deck +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2