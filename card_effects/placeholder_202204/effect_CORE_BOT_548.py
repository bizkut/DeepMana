"""Effect for Zilliax (CORE_BOT_548).

Card Text: <b>Magnetic</b>
<b><b>Divine Shield</b>, <b>Taunt</b>, Lifesteal, Rush</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass