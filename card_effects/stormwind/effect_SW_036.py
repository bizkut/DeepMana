"""Effect for Two-Faced Investor (SW_036).

Card Text: [x]At the end of your turn,
reduce the Cost of a card
in your hand by (1). <i>(50%
chance to increase.)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass