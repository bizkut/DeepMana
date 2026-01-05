"""Effect for Earth Elemental (EX1_250).

Card Text: <b>Taunt</b>
<b><b>Overload</b>:</b> (2)
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass