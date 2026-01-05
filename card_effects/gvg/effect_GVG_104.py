"""Effect for Hobgoblin (GVG_104).

Card Text: Whenever you play a 1-Attack minion, give it +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1