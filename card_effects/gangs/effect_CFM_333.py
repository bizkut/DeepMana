"""Effect for Knuckles (CFM_333).

Card Text: After this attacks a
minion, it also hits the enemy hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass