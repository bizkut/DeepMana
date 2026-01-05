"""Effect for Sphere of Sapience (SCH_259).

Card Text: [x]At the start of your turn,
look at your top card. You
can put it on the bottom
 and lose 1 Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass