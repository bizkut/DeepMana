"""Effect for Burgly Bully (CFM_669).

Card Text: Whenever your opponent casts a spell, add a Coin to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass