"""Effect for Auctionmaster Beardo (CFM_807).

Card Text: After you cast a spell, refresh your Hero Power.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass