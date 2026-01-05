"""Effect for Impatient Shopkeep (SW_055).

Card Text: <b>Tradeable</b>
<b>Rush</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass