"""Effect for Umbraclaw (EDR_227).

Card Text: <b>Rush</b>
<b>Deathrattle:</b> <b>Imbue</b> your Hero Power.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass