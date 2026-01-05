"""Effect for Weapons Expert (MAW_029).

Card Text: <b>Battlecry:</b> If you have a weapon equipped, give it +1/+1. Otherwise, draw a weapon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)