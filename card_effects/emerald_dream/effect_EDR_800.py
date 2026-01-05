"""Effect for Flutterwing Guardian (EDR_800).

Card Text: <b><b>Taunt</b>, Divine Shield</b>
<b>Battlecry:</b> <b>Imbue</b> your Hero Power.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass