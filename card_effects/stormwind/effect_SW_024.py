"""Effect for Lothar (SW_024).

Card Text: At the end of your turn, attack a random enemy minion. If it dies, gain +3/+3.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3