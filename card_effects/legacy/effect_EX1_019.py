"""Effect for Shattered Sun Cleric (EX1_019).

Card Text: <b>Battlecry:</b> Give a friendly minion +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1