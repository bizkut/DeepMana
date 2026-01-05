"""Effect for Witch's Cauldron (GIL_819).

Card Text: After a friendly minion dies, add a random Shaman spell to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass