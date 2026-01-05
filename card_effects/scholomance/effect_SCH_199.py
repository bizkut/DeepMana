"""Effect for Transfer Student (SCH_199).

Card Text: This has different effects based on which game board you're on.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass