"""Effect for Plucky Podling (EDR_529).

Card Text: [x]If this would transform into
a minion, it transforms into
one that costs (2) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass