"""Effect for Drakkari Defender (CORE_ICC_081).

Card Text: <b>Taunt</b>
<b>Overload:</b> (3)
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass