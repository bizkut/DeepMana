"""Effect for Bronze Gatekeeper (CORE_BOT_021).

Card Text: <b>Magnetic</b>
<b>Taunt</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass