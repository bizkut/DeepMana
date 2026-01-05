"""Effect for Potionmaster Putricide (RLK_572).

Card Text: After a minion dies, add a Concoction to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass