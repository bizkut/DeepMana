"""Effect for Piranha Poacher (TSC_633).

Card Text: At the end of your turn,
add a 1/1 Piranha Swarmer to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass