"""Effect for Ogre Brute (GVG_065).

Card Text: 50% chance to attack the wrong enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass