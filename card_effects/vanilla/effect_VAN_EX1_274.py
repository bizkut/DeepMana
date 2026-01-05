"""Effect for Ethereal Arcanist (VAN_EX1_274).

Card Text: If you control a <b>Secret</b> at the end of your turn, gain +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2