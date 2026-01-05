"""Effect for Pint-Sized Summoner (EX1_076).

Card Text: The first minion you play each turn costs (1) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass