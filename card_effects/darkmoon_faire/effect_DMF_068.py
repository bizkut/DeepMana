"""Effect for Optimistic Ogre (DMF_068).

Card Text: 50% chance to attack the correct enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass