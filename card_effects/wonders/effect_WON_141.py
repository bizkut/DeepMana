"""Effect for Menagerie Mug (WON_141).

Card Text: [x]<b>Battlecry:</b> Give 3 random
friendly minions of different
minion types +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3