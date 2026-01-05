"""Effect for Cheesemonger (SW_073).

Card Text: [x]Whenever your opponent
casts a spell, add a random
spell with the same Cost
to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass