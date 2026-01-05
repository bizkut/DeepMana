"""Effect for Beryllium Nullifier (BOT_237).

Card Text: <b>Magnetic</b>
<b>Elusive</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass