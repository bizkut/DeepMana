"""Effect for Gyrocopter (DRG_061).

Card Text: <b>Rush</b>
<b>Windfury</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass