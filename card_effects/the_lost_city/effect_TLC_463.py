"""Effect for Razidir (TLC_463).

Card Text: [x]<b>Battlecry:</b> Discard a random
card from your hand.
<b>Kindred:</b> Your opponent's
hand instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass