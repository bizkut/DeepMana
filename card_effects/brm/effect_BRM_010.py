"""Effect for Druid of the Flame (BRM_010).

Card Text: <b>Choose One -</b> Transform into a 5/2 minion; or a 2/5 minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass