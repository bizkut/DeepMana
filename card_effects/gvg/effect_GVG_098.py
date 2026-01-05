"""Effect for Gnomeregan Infantry (GVG_098).

Card Text: <b>Charge</b>
<b>Taunt</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass