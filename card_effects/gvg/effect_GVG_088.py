"""Effect for Ogre Ninja (GVG_088).

Card Text: <b>Stealth</b>
50% chance to attack the wrong enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass