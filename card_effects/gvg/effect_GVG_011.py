"""Effect for Shrinkmeister (GVG_011).

Card Text: <b>Battlecry:</b> Give a minion -3 Attack this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3