"""Effect for Chillblade Champion (CORE_ICC_820).

Card Text: <b>Charge</b>
<b>Lifesteal</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass