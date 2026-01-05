"""Effect for Bitterbloom Knight (EDR_852).

Card Text: <b>Battlecry:</b> <b>Imbue</b> your
Hero Power.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass