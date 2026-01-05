"""Effect for Dunemaul Shaman (GVG_066).

Card Text: <b>Windfury, Overload:</b> (1)
50% chance to attack the wrong enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass