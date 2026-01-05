"""Effect for Cave Hydra (LOOT_078).

Card Text: Also damages the minions next to whomever
this attacks.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass