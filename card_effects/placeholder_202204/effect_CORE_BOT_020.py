"""Effect for Skaterbot (CORE_BOT_020).

Card Text: <b>Magnetic</b>
<b>Rush</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass