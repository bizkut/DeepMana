"""Effect for Dinositter (TLC_822).

Card Text: [x]At the end of your
turn, reduce the Cost
of a random Beast in
your hand by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass