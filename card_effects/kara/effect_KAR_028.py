"""Effect for Fool's Bane (KAR_028).

Card Text: Unlimited attacks each turn. Can't attack heroes.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass