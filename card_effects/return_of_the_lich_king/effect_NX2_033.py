"""Effect for Thaddius, Monstrosity (NX2_033).

Card Text: [x]<b>Taunt</b>. Your odd-Cost
cards cost (2) less. <i>(Swaps
polarity each turn!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass