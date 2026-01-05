"""Effect for Scaled Nightmare (OG_271).

Card Text: At the start of your turn, double this minion's Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass