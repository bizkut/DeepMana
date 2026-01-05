"""Effect for Flamereaper (BT_271).

Card Text: Also damages the minions next to whomever your hero attacks.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass