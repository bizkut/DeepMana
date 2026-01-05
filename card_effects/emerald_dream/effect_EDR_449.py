"""Effect for Lunarwing Messenger (EDR_449).

Card Text: <b>Lifesteal</b>
<b>Battlecry:</b> <b>Imbue</b> your Hero Power.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass