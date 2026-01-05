"""Effect for Lynessa Sunsorrow (LOOT_216).

Card Text: [x]<b>Battlecry:</b> Cast each spell
you cast on your minions
 this game on this one.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass