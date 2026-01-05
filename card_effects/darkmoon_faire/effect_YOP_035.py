"""Effect for Moonfang (YOP_035).

Card Text: Can only take 1 damage at a time.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass