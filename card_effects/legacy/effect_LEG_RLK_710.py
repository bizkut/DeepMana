"""Effect for Rimefang Sword (LEG_RLK_710).

Card Text: [x]After your hero attacks,
reduce the Cost of a spell
in your hand by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass