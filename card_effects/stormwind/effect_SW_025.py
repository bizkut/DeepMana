"""Effect for Auctionhouse Gavel (SW_025).

Card Text: [x]After your hero attacks,
reduce the Cost of a
<b>Battlecry</b> minion in
your hand by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass