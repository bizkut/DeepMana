"""Effect for Sonya Shadowdancer (LOOT_165).

Card Text: After a friendly minion dies, add a 1/1 copy of it to your hand. It costs (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass