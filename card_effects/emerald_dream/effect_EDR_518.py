"""Effect for Living Garden (EDR_518).

Card Text: [x]<b>Battlecry:</b> <b>Imbue</b> your Hero
Power. Reduce the Cost of a
 minion in your hand by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass