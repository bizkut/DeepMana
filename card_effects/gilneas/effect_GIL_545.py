"""Effect for Ghostly Charger (GIL_545).

Card Text: <b>Divine Shield</b>
<b>Rush</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass