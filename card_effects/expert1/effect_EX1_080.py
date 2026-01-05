"""Effect for Secretkeeper (EX1_080).

Card Text: Whenever a <b>Secret</b> is played, gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1