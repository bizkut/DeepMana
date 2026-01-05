"""Effect for Goldwing (NX2_022).

Card Text: [x]<b>Rush</b>
<b>Battlecry:</b> If you're holding
a Mech, gain <b>Windfury</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass