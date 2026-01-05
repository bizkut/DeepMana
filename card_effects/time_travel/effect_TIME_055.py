"""Effect for Unknown Voyager (TIME_055).

Card Text: After this survives damage, transform into a random 7-Cost minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass