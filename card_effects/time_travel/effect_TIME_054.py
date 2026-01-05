"""Effect for Time Skipper (TIME_054).

Card Text: At the end of each player's turn, give them a Coin.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1