"""Effect for Saddlemaster (YOP_028).

Card Text: After you play a Beast, add a random Beast to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass