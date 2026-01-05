"""Effect for Swamp King Dred (UNG_919).

Card Text: After your opponent plays a minion, attack it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass