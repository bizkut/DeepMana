"""Effect for Feral Gibberer (LOOT_218).

Card Text: After this minion attacks a hero, add a copy of it to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass