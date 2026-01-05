"""Effect for Abominable Lieutenant (AV_139).

Card Text: At the end of your turn,
eat a random enemy minion and gain its stats.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass