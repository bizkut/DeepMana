"""Effect for Maiden of the Lake (AT_085).

Card Text: Your Hero Power costs (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass