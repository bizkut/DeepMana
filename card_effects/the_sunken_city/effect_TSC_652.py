"""Effect for Green-Thumb Gardener (TSC_652).

Card Text: [x]<b>Battlecry:</b> Refresh empty
Mana Crystals equal to the
Cost of the highest Cost
spell in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass