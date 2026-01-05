"""Effect for Wayward Sage (TSC_217).

Card Text: [x]<b>Outcast:</b> Reduce the Cost
of the left and right-most
 cards in your hand by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass