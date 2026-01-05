"""Effect for Menagerie Mug (CORE_WON_141).

Card Text: [x]<b>Battlecry:</b> Give 3 random friendly minions of different minion types +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
