"""Effect for Amani Berserker (VAN_EX1_393).

Card Text: <b>Enrage:</b> +3 Attack
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3