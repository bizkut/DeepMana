"""Effect for Costume Merchant (DINO_427).

Card Text: [x]<b>Battlecry:</b> Get a random
Mask from another class.
 <b>Combo:</b> It costs (2) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass