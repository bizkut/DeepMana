"""Effect for Grimestreet Enforcer (CFM_639).

Card Text: At the end of your turn, give all minions in your hand +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1