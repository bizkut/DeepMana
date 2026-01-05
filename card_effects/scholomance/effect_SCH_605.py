"""Effect for Lake Thresher (SCH_605).

Card Text: Also damages the minions next to whomever
this attacks.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass