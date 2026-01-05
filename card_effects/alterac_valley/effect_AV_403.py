"""Effect for Cera'thine Fleetrunner (AV_403).

Card Text: [x]<b>Battlecry:</b> Replace your
minions in hand and deck
 with ones from other classes.
They cost (2) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass