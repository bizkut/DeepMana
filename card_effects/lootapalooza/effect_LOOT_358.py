"""Effect for Grumble, Worldshaker (LOOT_358).

Card Text: <b>Battlecry:</b> Return your other minions to your hand. They cost (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass