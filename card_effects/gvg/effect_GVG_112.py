"""Effect for Mogor the Ogre (GVG_112).

Card Text: All minions have a 50% chance to attack the wrong enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass