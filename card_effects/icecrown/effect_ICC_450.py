"""Effect for Death Revenant (ICC_450).

Card Text: <b>Battlecry:</b> Gain +1/+1 for each damaged minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1