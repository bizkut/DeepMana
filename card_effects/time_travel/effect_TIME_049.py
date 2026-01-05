"""Effect for Dangerous Variant (TIME_049).

Card Text: At the start of your turn, transform into a random 5-Cost minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass