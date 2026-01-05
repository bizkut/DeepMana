"""Effect for Gurubashi Berserker (CORE_EX1_399).

Card Text: Whenever this minion takes damage, gain +3 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3