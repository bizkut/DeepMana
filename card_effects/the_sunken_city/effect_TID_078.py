"""Effect for Shattershambler (TID_078).

Card Text: [x]<b>Battlecry:</b> Your next
<b>Deathrattle</b> minion costs (1) 
 less, but immediately
dies when played.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass