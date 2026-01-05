"""Effect for Barista Lynchen (DAL_546).

Card Text: <b>Battlecry:</b> Add a copy of each of your other <b>Battlecry</b> minions to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass