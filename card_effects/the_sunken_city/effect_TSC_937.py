"""Effect for Crabatoa (TSC_937).

Card Text: <b>Colossal +2</b>
Your Crabatoa Claws have +2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2