"""Effect for Blackwater Behemoth (TSC_216).

Card Text: <b>Colossal +1</b>
<b>Lifesteal</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1