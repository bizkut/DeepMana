"""Effect for Ravencaller (GIL_212).

Card Text: [x]<b>Battlecry:</b> Add two
random 1-Cost minions
to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass