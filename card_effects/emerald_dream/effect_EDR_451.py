"""Effect for Goldpetal Drake (EDR_451).

Card Text: [x]<b>Battlecry and Deathrattle:</b>
<b>Imbue</b> your Hero Power.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass