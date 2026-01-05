"""Effect for Naga Sand Witch (ULD_435).

Card Text: [x]<b>Battlecry:</b> Change the Cost
of spells in your hand to (5).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass