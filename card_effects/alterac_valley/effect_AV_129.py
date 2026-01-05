"""Effect for Blood Guard (AV_129).

Card Text: Whenever this minion takes damage, give your minions +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1