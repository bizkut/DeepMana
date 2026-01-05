"""Effect for Tortollan Storyteller (TLC_254).

Card Text: [x]At the end of your turn,
give +1/+1 to each friendly
minion of a different type.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1