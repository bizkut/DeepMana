"""Effect for Tar Creeper (UNG_928).

Card Text: <b>Taunt</b>
Has +2 Attack during your opponent's turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2