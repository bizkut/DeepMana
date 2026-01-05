"""Effect for Angry Chicken (VAN_EX1_009).

Card Text: <b>Enrage:</b> +5 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 5
        target._max_health += 5