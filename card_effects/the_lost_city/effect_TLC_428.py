"""Effect for Hot Spring Glider (TLC_428).

Card Text: <b>Battlecry:</b> Your next
Murloc costs (1) less.
<b>Kindred:</b> And gains <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass