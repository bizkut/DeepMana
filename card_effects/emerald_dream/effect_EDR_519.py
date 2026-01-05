"""Effect for Wisprider (EDR_519).

Card Text: <b>Battlecry:</b> <b>Imbue</b> your Hero Power, then trigger it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass