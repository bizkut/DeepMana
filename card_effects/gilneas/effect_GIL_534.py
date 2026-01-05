"""Effect for Hench-Clan Thug (GIL_534).

Card Text: After your hero attacks, give this minion +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1