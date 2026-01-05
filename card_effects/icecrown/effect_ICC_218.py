"""Effect for Howlfiend (ICC_218).

Card Text: Whenever this minion takes damage, discard a random card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass