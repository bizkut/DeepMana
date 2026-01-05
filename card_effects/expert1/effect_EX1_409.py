"""Effect for Upgrade! (EX1_409).

Card Text: If you have a weapon, give it +1/+1. Otherwise equip a 1/3 weapon.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1