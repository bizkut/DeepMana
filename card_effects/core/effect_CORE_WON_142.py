"""Effect for Menagerie Jug (CORE_WON_142).

Card Text: [x]<b>Battlecry:</b> Give 3 random friendly minions of different minion types +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
