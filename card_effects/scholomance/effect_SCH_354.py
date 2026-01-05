"""Effect for Ancient Void Hound (SCH_354).

Card Text: [x]At the end of your turn,
steal 1 Attack and Health
from all enemy minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)