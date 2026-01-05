"""Effect for Hamuul Runetotem (EDR_845).

Card Text: [x]<b>Start of Game:</b> If each spell
in your deck is Nature, <b>Imbue</b>
your Hero Power. Repeat this
 every 2 spells you cast.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass