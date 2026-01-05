"""Effect for Evasive Wyrm (DRG_079).

Card Text: <b>Rush</b>
<b>Divine Shield</b>
<b>Elusive</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass