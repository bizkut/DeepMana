"""Effect for Blackjack Stunner (BT_711).

Card Text: [x]<b>Battlecry:</b> If you control a
<b>Secret</b>, return a minion
to its owner's hand.
It costs (2) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass