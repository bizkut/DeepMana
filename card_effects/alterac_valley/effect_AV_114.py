"""Effect for Shivering Sorceress (AV_114).

Card Text: [x]<b>Battlecry:</b> Reduce the Cost
of the highest Cost spell
in your hand by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass