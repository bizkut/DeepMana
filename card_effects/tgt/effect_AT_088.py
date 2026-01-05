"""Effect for Mogor's Champion (AT_088).

Card Text: 50% chance to attack the wrong enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass