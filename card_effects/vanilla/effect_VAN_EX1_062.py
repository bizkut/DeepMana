"""Effect for Old Murk-Eye (VAN_EX1_062).

Card Text: <b>Charge</b>. Has +1 Attack for each other Murloc on the battlefield.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1