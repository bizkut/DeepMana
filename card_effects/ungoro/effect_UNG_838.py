"""Effect for Tar Lord (UNG_838).

Card Text: <b>Taunt</b>
Has +4 Attack during your opponent's turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4