"""Effect for Banana Vendor (DMF_065).

Card Text: <b>Battlecry:</b> Add 2 Bananas to each player's hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass