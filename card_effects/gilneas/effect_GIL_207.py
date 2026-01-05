"""Effect for Phantom Militia (GIL_207).

Card Text: <b>Echo</b>
<b>Taunt</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass