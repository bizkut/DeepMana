"""Effect for Wargear (CORE_BOT_563).

Card Text: <b>Magnetic</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass