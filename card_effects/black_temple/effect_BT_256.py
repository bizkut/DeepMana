"""Effect for Dragonmaw Overseer (BT_256).

Card Text: At the end of your turn, give another friendly minion +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2