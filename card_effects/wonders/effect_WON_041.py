"""Effect for Chromie, Timehopper (WON_041).

Card Text: [x]<b>Battlecry:</b> Visit a Historical 
Epoch. Shuffle the others
 into your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass