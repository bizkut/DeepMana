"""Effect for Venomizer (BOT_035).

Card Text: <b>Magnetic</b>
<b>Poisonous</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass