"""Effect for Prince Liam (GIL_694).

Card Text: [x]<b>Battlecry:</b> Transform all
1-Cost cards in your deck
 into <b>Legendary</b> minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass