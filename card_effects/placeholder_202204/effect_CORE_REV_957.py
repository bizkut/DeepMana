"""Effect for Murlocula (CORE_REV_957).

Card Text: <b>Lifesteal</b>
<b>Infuse (4):</b> This costs (0).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass