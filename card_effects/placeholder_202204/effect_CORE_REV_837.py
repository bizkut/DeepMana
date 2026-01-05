"""Effect for Muck Plumber (CORE_REV_837).

Card Text: ALL minions cost (2) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass